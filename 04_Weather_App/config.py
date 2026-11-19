
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read API key
API_KEY = os.getenv("WEATHER_API_KEY")

# Check whether API key exists
if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")
