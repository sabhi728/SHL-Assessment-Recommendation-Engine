from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import numpy as np
import json
from pathlib import Path
import os
from dotenv import load_dotenv
import logging
import traceback

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="SHL Assessment Recommendation Engine")

# Configure CORS with more detailed settings
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "https://*.onrender.com",  # Allow Render deployments
    "*"  # Allow all origins for testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure static and templates directories exist
Path("static").mkdir(exist_ok=True)
Path("templates").mkdir(exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Ensure data and models directories exist
Path("data").mkdir(exist_ok=True)
Path("models").mkdir(exist_ok=True)

try:
    # Load model configuration
    with open("models/config.json") as f:
        MODEL_CONFIG = json.load(f)
        logger.debug(f"Model config loaded: {MODEL_CONFIG}")

    # Load SHL product catalog
    with open("data/shl_products.json") as f:
        data = json.load(f)
        PRODUCTS = data["products"]
        logger.debug(f"Loaded {len(PRODUCTS)} products")
except Exception as e:
    logger.error(f"Error loading configuration files: {str(e)}")
    MODEL_CONFIG = {
        "model_settings": {
            "transformer_model": "sentence-transformers/all-MiniLM-L6-v2",
            "max_sequence_length": 128,
            "weights": {
                "semantic_similarity": 0.4,
                "role_match": 0.3,
                "category_match": 0.3
            }
        },
        "role_matching": {
            "exact_match_score": 1.0,
            "partial_match_score": 0.5,
            "no_match_score": 0.0
        },
        "category_matching": {
            "min_categories_match": 1,
            "boost_multiple_matches": True
        }
    }
    PRODUCTS = []

API_PORT = int(os.getenv("PORT", "10000"))  # Changed from API_PORT to PORT for Render compatibility

# Add server configuration
SERVER_CONFIG = {
    "host": "0.0.0.0",
    "port": API_PORT,
    "reload": False,  # Disable reload in production
    "workers": 1,
    "log_level": "info"
}

class RecommendationRequest(BaseModel):
    job_role: str
    assessment_needs: List[str]
    experience_level: Optional[str] = None

class RecommendationResponse(BaseModel):
    recommended_products: List[dict]
    confidence_scores: List[float]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "products_loaded": len(PRODUCTS) > 0,
        "config_loaded": MODEL_CONFIG is not None
    }

@app.get("/products")
async def get_products():
    return PRODUCTS

@app.post("/recommend")
async def recommend(request: RecommendationRequest):
    try:
        logger.debug(f"Received recommendation request: {request}")
        
        # Convert input to lowercase for case-insensitive matching
        job_role = request.job_role.lower()
        assessment_needs = [need.lower() for need in request.assessment_needs if need]  # Filter out empty strings
        experience_level = request.experience_level.lower() if request.experience_level else None

        logger.debug(f"Processed request - job_role: {job_role}, needs: {assessment_needs}, level: {experience_level}")

        recommended = []
        confidence_scores = []

        for product in PRODUCTS:
            score = 0.0
            matches = 0

            # Check role match
            product_roles = [role.lower() for role in product["suitable_roles"]]
            if any(role in job_role for role in product_roles) or any(job_role in role for role in product_roles):
                score += 0.4
                matches += 1
                logger.debug(f"Role match found for product {product['name']}")

            # Check category match
            product_categories = [cat.lower() for cat in product["categories"]]
            category_matches = sum(1 for need in assessment_needs if any(cat in need.lower() or need.lower() in cat for cat in product_categories))
            if category_matches > 0:
                score += 0.3 * (category_matches / len(assessment_needs))
                matches += 1
                logger.debug(f"Category match found for product {product['name']}")

            # Check experience level match if provided
            if experience_level and "experience_levels" in product:
                if experience_level in product["experience_levels"]:
                    score += 0.3
                    matches += 1
                    logger.debug(f"Experience level match found for product {product['name']}")

            # Only include products with at least one match
            if matches > 0:
                recommended.append(product)
                confidence_scores.append(score)
                logger.debug(f"Added product {product['name']} with score {score}")

        # Sort by confidence score
        sorted_indices = np.argsort(confidence_scores)[::-1]
        recommended = [recommended[i] for i in sorted_indices]
        confidence_scores = [confidence_scores[i] for i in sorted_indices]

        logger.debug(f"Returning {len(recommended)} recommendations")
        return RecommendationResponse(
            recommended_products=recommended,
            confidence_scores=confidence_scores
        )

    except Exception as e:
        logger.error(f"Error in recommendation: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test")
async def test(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/api/test")
async def api_test():
    return {"status": "ok", "message": "API is working"}

if __name__ == "__main__":
    import uvicorn
    try:
        logger.info(f"Starting server on {SERVER_CONFIG['host']}:{SERVER_CONFIG['port']}")
        logger.info(f"Environment: {os.getenv('ENVIRONMENT', 'production')}")
        logger.info(f"Products loaded: {len(PRODUCTS)}")
        logger.info(f"Model config loaded: {MODEL_CONFIG is not None}")
        
        # Use the app directly instead of the module string for Render
        uvicorn.run(
            app,
            host=SERVER_CONFIG["host"],
            port=SERVER_CONFIG["port"],
            reload=SERVER_CONFIG["reload"],
            workers=SERVER_CONFIG["workers"],
            log_level=SERVER_CONFIG["log_level"]
        )
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise 