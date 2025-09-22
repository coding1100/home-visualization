import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
COMFYUI_SERVER = os.environ.get("COMFYUI_SERVER", "http://127.0.0.1:8188")
RF_API_KEY = os.getenv("RF_API_KEY")
hf_token = os.getenv("HF_TOKEN")
FIXED_SEED = int(os.environ.get("FIXED_SEED", "-1"))

# Cache for workflow to avoid repeated loading
cached_workflow = None

# logger.info(f"UPLOAD_DIR: {UPLOAD_DIR}")
# logger.info(f"COMFYUI_SERVER: {COMFYUI_SERVER}")
# logger.info(f"RF_API_KEY: {RF_API_KEY}")
# logger.info(f"HF_TOKEN: {HF_TOKEN}")