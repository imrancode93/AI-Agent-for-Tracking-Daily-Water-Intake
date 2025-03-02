import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Database Config
DB_URL = "sqlite:///water_tracker.db"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
