# test_env.py
from dotenv import load_dotenv
import os

# Ensure you have python-dotenv installed in your virtual environment
# pip install python-dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
env = os.getenv('ENVIRONMENT')

print(f"API key loaded: {'Yes' if api_key else 'No'}")
print(f"Environment: {env}")