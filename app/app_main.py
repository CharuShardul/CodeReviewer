# app/app_main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import app.utils as utils
import app.ollama_agent as ollama_agent

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("app.log", mode="a"), 
                              logging.StreamHandler()]) 

app = FastAPI()
logger = logging.getLogger(__name__)

# Define the directory containing the sample codebase
directory = r"test\sample_codebase" # Adjust the path as needed
# Ensure the directory exists
if not utils.read_files(directory):
    logger.error(f"Directory {directory} does not exist or contains no Python files.")
    raise HTTPException(status_code=404, detail=f"Directory {directory} does not exist or contains no Python files.")

# Initialize the Ollama API client once
model_name = "llama3.1:8b"
ollama_agent_instance = ollama_agent.LlamaCodeReviewAgent(model_name=model_name)

class CodeFile(BaseModel):
    filename: str
    content: str

@app.post("/review")
def review_code(file: CodeFile):
    """
    Review a single Python file.
    """
    try:
        response = ollama_agent_instance.review_code(file.filename, file.content)
        return {"filename": file.filename, "review": response}
    except Exception as e:
        logger.error(f"Error reviewing file {file.filename}: {e}")
        raise HTTPException(status_code=500, detail=f"Error reviewing file {file.filename}: {e}")

@app.get("/review-all")
def review_all_files():
    """
    Review all Python files in the sample codebase.
    """
    files_content = utils.read_files()
    if not files_content:
        logger.error("No Python files found to review.")
        raise HTTPException(status_code=404, detail="No Python files found to review.")
    reviews = {}
    for filename, content in files_content.items():
        try:
            review = ollama_agent_instance.review_code(filename, content)
            reviews[filename] = review
        except Exception as e:
            logger.error(f"Error reviewing file {filename}: {e}")
            reviews[filename] = f"Error: {e}"
    return {"reviews": reviews}