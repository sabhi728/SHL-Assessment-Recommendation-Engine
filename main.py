from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Dict, Any
import json
import logging
from sentence_transformers import SentenceTransformer
import numpy as np
from pathlib import Path
import os
from dotenv import load_dotenv
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
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

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load the sentence transformer model
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    logger.info("Sentence transformer model loaded successfully")
except Exception as e:
    logger.error(f"Error loading sentence transformer model: {str(e)}")
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

assessments = load_assessments()

class RecommendationRequest(BaseModel):
    query: str

class Assessment(BaseModel):
    url: str
    adaptive_support: str
    description: str
    duration: int
    remote_support: str
    test_type: List[str]

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

def get_recommendations(query: str) -> List[Dict]:
    """Get recommendations based on query"""
    try:
        # Calculate similarity scores for all assessments
        scored_assessments = []
        for assessment in assessments:
            # Calculate similarity score
            similarity_score = calculate_similarity(query, assessment["description"])
            
            scored_assessments.append({
                **assessment,
                "similarity_score": similarity_score
            })
        
        # Sort by score and return top 10
        scored_assessments.sort(key=lambda x: x["similarity_score"], reverse=True)
        top_assessments = scored_assessments[:10]
        logger.info(f"Returning {len(top_assessments)} top recommendations")
        return top_assessments
    
    except Exception as e:
        logger.error(f"Error getting recommendations: {str(e)}")
        logger.error(traceback.format_exc())
        return []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }

@app.post("/recommend", response_model=RecommendationResponse)
async def recommend(request: RecommendationRequest):
    try:
        logger.info(f"Received recommendation request with query: {request.query[:50]}...")
        
        recommendations = get_recommendations(request.query)
        logger.info(f"Returning {len(recommendations)} recommendations")
        
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations found")
        
        return RecommendationResponse(recommended_assessments=recommendations)
    except Exception as e:
        logger.error(f"Error in recommendation endpoint: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 