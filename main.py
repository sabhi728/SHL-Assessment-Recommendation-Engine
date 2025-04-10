from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import json
import logging
from sentence_transformers import SentenceTransformer
import numpy as np
from pathlib import Path
import os
from dotenv import load_dotenv
import traceback
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="SHL Assessment Recommendation Engine",
    description="API for recommending SHL assessments based on job descriptions and filters",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Global variables for model and assessments
model = None
assessments = []

@app.on_event("startup")
async def startup_event():
    global model, assessments
    try:
        # Load the sentence transformer model
        model = SentenceTransformer('all-MiniLM-L6-v2')
        logger.info("Sentence transformer model loaded successfully")
        
        # Load assessments data
        assessments = load_assessments()
        logger.info(f"Loaded {len(assessments)} assessments successfully")
    except Exception as e:
        logger.error(f"Error during startup: {str(e)}")
        logger.error(traceback.format_exc())
        raise

# Load assessments data
def load_assessments():
    try:
        with open("data/shl_products.json", "r") as f:
            data = json.load(f)
            assessments = data.get("assessments", [])
            logger.info(f"Loaded {len(assessments)} assessments successfully")
            return assessments
    except FileNotFoundError:
        logger.error("Assessment data file not found")
        return []
    except json.JSONDecodeError:
        logger.error("Invalid JSON format in assessment data file")
        return []
    except Exception as e:
        logger.error(f"Error loading assessments: {str(e)}")
        return []

class Filters(BaseModel):
    duration: Optional[int] = None
    adaptive_support: Optional[str] = None
    remote_support: Optional[str] = None
    test_type: Optional[List[str]] = None

class RecommendationRequest(BaseModel):
    query: str
    filters: Optional[Filters] = None

class Assessment(BaseModel):
    url: str
    adaptive_support: str
    description: str
    duration: int
    remote_support: str
    test_type: List[str]
    similarity_score: float

class RecommendationResponse(BaseModel):
    recommended_assessments: List[Assessment]

def calculate_similarity(query: str, description: str) -> float:
    """Calculate similarity score between query and description"""
    try:
        query_embedding = model.encode(query)
        description_embedding = model.encode(description)
        similarity = float(np.dot(query_embedding, description_embedding))
        logger.debug(f"Similarity score calculated: {similarity}")
        return similarity
    except Exception as e:
        logger.error(f"Error calculating similarity: {str(e)}")
        return 0.0

def get_recommendations(query: str, filters: Optional[Filters] = None) -> List[Dict]:
    """Get recommendations based on query and filters"""
    try:
        if not query or not query.strip():
            raise ValueError("Query cannot be empty")

        # Calculate similarity scores for all assessments
        scored_assessments = []
        for assessment in assessments:
            # Apply filters if provided
            if filters:
                # Duration filter
                if filters.duration is not None and assessment['duration'] > filters.duration:
                    continue
                
                # Adaptive support filter
                if filters.adaptive_support and assessment['adaptive_support'] != filters.adaptive_support:
                    continue
                
                # Remote support filter
                if filters.remote_support and assessment['remote_support'] != filters.remote_support:
                    continue
                
                # Test type filter - check if any of the selected test types match
                if filters.test_type:
                    assessment_test_types = [t.lower() for t in assessment['test_type']]
                    selected_test_types = [t.lower() for t in filters.test_type]
                    if not any(test_type in assessment_test_types for test_type in selected_test_types):
                        continue

            # Calculate similarity score
            similarity_score = calculate_similarity(query, assessment["description"])
            
            # Only add assessments with positive similarity score
            if similarity_score > 0:
                scored_assessments.append({
                    **assessment,
                    "similarity_score": similarity_score
                })
        
        # Sort by score and return all matching results
        scored_assessments.sort(key=lambda x: x["similarity_score"], reverse=True)
        logger.info(f"Returning {len(scored_assessments)} recommendations")
        return scored_assessments
    
    except Exception as e:
        logger.error(f"Error getting recommendations: {str(e)}")
        logger.error(traceback.format_exc())
        return []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    try:
        return {
            "status": "healthy",
            "assessments_loaded": len(assessments) > 0,
            "model_loaded": model is not None,
            "environment": os.getenv("ENVIRONMENT", "production")
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }

@app.post("/recommend", response_model=RecommendationResponse)
async def recommend(request: RecommendationRequest):
    try:
        if not request.query or not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")
            
        logger.info(f"Received recommendation request with query: {request.query[:50]}...")
        logger.info(f"Filters: {request.filters}")
        
        recommendations = get_recommendations(request.query, request.filters)
        logger.info(f"Returning {len(recommendations)} recommendations")
        
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations found matching your criteria")
        
        return RecommendationResponse(recommended_assessments=recommendations)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in recommendation endpoint: {str(e)}")
        logger.error(traceback.format_exc())
        return JSONResponse(
            status_code=500,
            content={"detail": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 