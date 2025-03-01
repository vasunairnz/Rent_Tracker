"" 
from dotenv import load_dotenv
import os

# Load variables from .env into environment variables
load_dotenv()

# Assign variables from environment
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
