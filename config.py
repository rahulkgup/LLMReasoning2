# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_api_key():
    """
    Retrieves the OpenAI API key from environment variables.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key