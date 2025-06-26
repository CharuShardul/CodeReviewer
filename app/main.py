# app/main.py

import ollama
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("app.log", mode="a"), 
                              logging.StreamHandler()]) 

import utils
import ollama_agent

logger = logging.getLogger(__name__)


def main():
    """
    Main function to initialize the Ollama API client and review Python files in 
    the sample codebase.
    """ 
    # Initialize the Ollama API client
    model_name = "llama3.1:8b"
    logger.info("Starting Ollama API client...")
    agent = ollama_agent.LlamaCodeReviewAgent(model_name=model_name)
    logger.info(f"Using the model: {agent.model_name}")

    # Read files from the sample codebase
    logger.info("Reading files from the sample codebase...")
    directory = r"test\sample_codebase" # Adjust the path as needed
    files_content = utils.read_files(directory)

    logger.info(f"Found {len(files_content)} Python files to review.")

    if not files_content:
        logger.error("No Python files found to review.")
        
    for filename, content in files_content.items():
        logger.info(f"Reviewing file: {filename}")
        logger.info(f"response = {agent.review_code(filename, content)}")
        try:
            response = agent.review_code(filename, content)
            logger.info(f"Review for {filename}:\n{response}")
        except Exception as e:
            logger.error(f"Error reviewing file {filename}: {e}")


if __name__ == "__main__":
    main()        