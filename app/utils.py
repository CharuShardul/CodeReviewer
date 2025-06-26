import os
import logging 

logger = logging.getLogger(__name__)

def read_files(directory: str = r"test\sample_codebase") -> dict:
    """
    Reads all Python files in the specified directory and returns their contents.

    Args:
        directory (str): The path to the directory containing Python files.

    Returns:
        dict: A dictionary where keys are filenames and values are file contents.
    """
    logger.info(f"Reading Python files from directory: {directory}")
    if not os.path.exists(directory):
        logger.error(f"Directory {directory} does not exist.")
        return {}
    files_content = {}
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    files_content[filename] = file.read()
        logger.info(f"Successfully read {len(files_content)} Python files from {directory}")
    except Exception as e:
        logger.error(f"Error reading files from {directory}: {e}")
    return files_content 