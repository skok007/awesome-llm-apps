import os
from dotenv import load_dotenv

# Initialize OPENAI_API_KEY as None at module level
OPENAI_API_KEY = None

def setup_environment():
    # Load the OpenAI API key from .openai_key file
    with open('.openai_key', 'r') as f:
        api_key = f.read().strip()
        # Extract the key value if it's in the format OPENAI_API_KEY=sk-...
        if '=' in api_key:
            api_key = api_key.split('=')[1].strip()
    
    # Set the API key as an environment variable
    os.environ['OPENAI_API_KEY'] = api_key
    
    # Set the global variable
    global OPENAI_API_KEY
    OPENAI_API_KEY = api_key
    
    print("Environment setup complete!")

if __name__ == "__main__":
    setup_environment() 