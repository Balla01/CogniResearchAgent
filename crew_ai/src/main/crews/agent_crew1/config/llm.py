from crewai import LLM
import os
from pathlib import Path
import dotenv
# Load environment variables
env_path = "./.env"
dotenv.load_dotenv(env_path)

# ---- LLM Configuration ----
ollama_flag = False
if ollama_flag:
    llm = LLM(
        model="ollama/llama3.2:1b",
        base_url="http://localhost:11434",
        temperature=0.7
    )
else:
    llm = LLM(
        model="mistral/mistral-large-latest",
        temperature=0.7,
        api_key = os.getenv("MISTRAL_API_KEY")
    )
