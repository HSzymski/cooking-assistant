import os
from dotenv import load_dotenv

# Load environment variables from .env file
#TODO: Change to .env in production
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env.dev'))
load_dotenv(dotenv_path, override=True)

def get_dotenv_variable(key: str) -> str | None:
    # Retrieve the value of an environment variable or raise an error
    value = os.getenv(key)

    if value is None:
        raise ValueError(f"Environment variable '{key}' not found")
    return value

# API keys
OPENAI_API_KEY = get_dotenv_variable("OPENAI_API_KEY")