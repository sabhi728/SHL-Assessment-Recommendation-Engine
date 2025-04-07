import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

# API Configuration
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))

# Model Configuration
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
MAX_SEQUENCE_LENGTH = 128

# SHL API Configuration
SHL_API_KEY = os.getenv("SHL_API_KEY")
SHL_API_BASE_URL = os.getenv("SHL_API_BASE_URL", "https://api.shl.com/v1")

# Recommendation Settings
MIN_CONFIDENCE_SCORE = 0.5
MAX_RECOMMENDATIONS = 5 