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
CLOUDINARY_FOLDER = "renders"
MATERIAL_PROMINENCE = os.getenv("MATERIAL_PROMINENCE", 0.7)

# Cache for workflow to avoid repeated loading
cached_workflow = None
# ====== GEOMETRY / MASK HELPERS ======
MAX_OUTPUT_IMAGE_MB = 2.0
MIN_OUTPUT_DIMENSION_PX = 720
_MB_DIVISOR = 1024 * 1024
DEFAULT_EXCLUDE_TYPES = {
    "window",
    "window frame",
    "window trim",
    "glass",
    "door",
    "garage",
    "garage door",
    "light",
    "lamp",
    "frame",
    "trim",
    "pillar",
    "column",
    "post",
    "stone",
    "foundation",
    "fence",
    "shutter",
    "railing",
    "gutter",
    "downspout",
    "soffit",
    "sofit",
    "fascia",
    "roof",
    "awning",
}
