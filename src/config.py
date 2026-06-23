from pathlib import Path
import os
from dotenv import load_dotenv

# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()

# -----------------------------------
# Project root (anchor point)
# -----------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# -----------------------------------
# Common directories
# -----------------------------------
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# -----------------------------------
# Database configuration
# -----------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env")