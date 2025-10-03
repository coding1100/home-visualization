import os
from huggingface_hub import login
from roboflow import Roboflow
from app.core.config import settings

from src.logger import logger
# from src.constants import RF_API_KEY, hf_token

def init_huggingface():
    try:
        # Try to use token from environment variable first
        if settings.HF_TOKEN:
            logger.info("Logging into Hugging Face Hub using token from environment variable")
            login(token=settings.HF_TOKEN)
        else:
            # Check if token file exists
            token_path = os.path.expanduser("~/.cache/huggingface/token")
            if os.path.exists(token_path):
                logger.info("Hugging Face token file found, using existing authentication")
            else:
                # Use default read-only token as fallback
                default_token = "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"  # Replace with your actual default token
                logger.warning("No Hugging Face token found. Using default read-only token.")
                logger.warning("This token has limited access. For full access, set the HF_TOKEN environment variable or run 'huggingface-cli login'")
                login(token=default_token)
    except Exception as e:
        logger.error(f"Error during Hugging Face authentication: {str(e)}")
        logger.warning("Continuing without Hugging Face authentication")

# Initialize Hugging Face authentication
init_huggingface()


# Initialize Roboflow model
# rf = Roboflow(api_key = os.getenv("RF_API_KEY"))
rf = Roboflow(api_key = settings.RF_API_KEY)
project = rf.workspace().project(settings.RF_MODEL_PROJECT)
model = project.version(settings.RF_MODEL_PROJECT_VERSION).model
