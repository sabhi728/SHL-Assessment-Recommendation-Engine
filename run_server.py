import uvicorn
import sys
import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def check_directories():
    """Ensure required directories exist"""
    required_dirs = ['static', 'templates', 'data', 'models']
    for dir_name in required_dirs:
        try:
            Path(dir_name).mkdir(exist_ok=True)
            logger.debug(f"Checked directory: {dir_name}")
        except Exception as e:
            logger.error(f"Error creating directory {dir_name}: {str(e)}")
            raise

def check_files():
    """Check if required files exist"""
    required_files = {
        "data/shl_products.json": "Product catalog",
        "models/config.json": "Model configuration"
    }
    
    for file_path, description in required_files.items():
        if not Path(file_path).exists():
            logger.error(f"Required file missing: {description} at {file_path}")
            raise FileNotFoundError(f"Required file missing: {description} at {file_path}")
        else:
            logger.debug(f"Found {description} at {file_path}")

def main():
    """Run the FastAPI server"""
    try:
        # Check environment
        logger.info("Starting server initialization...")
        check_directories()
        check_files()
        
        # Run server
        logger.info("Starting Uvicorn server...")
        uvicorn.run(
            app="main:app",
            host="0.0.0.0",  # Listen on all interfaces
            port=8080,
            reload=False,
            workers=1,
            log_level="debug"
        )
    except Exception as e:
        logger.error(f"Error starting server: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 