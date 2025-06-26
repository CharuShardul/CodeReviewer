# Python Code Reviewer

This is a simple project to illustrate how powerful locally run LLM models can be for specifically tailored tasks. It is Python-based code review tool that uses the [Ollama](https://ollama.com/) application and library to automatically review Python files for sensitive information, bad variable names, and credential leaks. It also rates the quality of each code file on a scale of 10. The project provides both a command-line interface and a FastAPI-powered web API for scalable, automated code reviews.

---

## Features

- **Automated code review** using Llama 3.1 8B model via Ollama.
- **Detects**:  
  - Hardcoded sensitive information (API keys, usernames, passwords, tokens, etc.)
  - Non-contextual or misleading variable names
  - Possible credential or configuration leaks
- **REST API** endpoints for reviewing single files or entire codebases.
- **Detailed logging** to `app.log` and console.

---

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally

---

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repo-url>
    cd llama_code_reviewer
    ```

2. **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Install and run Ollama:**

    - Download and install Ollama from [https://ollama.com/download](https://ollama.com/download).
    - Start the Ollama server:
        ```sh
        ollama serve
        ```
    - Pull the required Llama model:
        ```sh
        ollama pull llama3.1:8b
        ```

---

## Usage

There are two ways to use this tool.

### 1. Running on terminal

```sh
python app/main.py
```

### 2. Running on localhost using FastAPI
#### 1. **Run the FastAPI server**

```sh
uvicorn app.app_main:app --reload
```

- The API will be available at [http://localhost:8000](http://localhost:8000)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

#### 2. **API Endpoints**

- **POST `/review`**  
  Review a single Python file.
  - Request body:
    ```json
    {
      "filename": "example.py",
      "content": "print('hello world')"
    }
    ```
  - Response:
    ```json
    {
      "filename": "example.py",
      "review": "<review text>"
    }
    ```

- **GET `/review-all`**  
  Review all Python files in the `test/sample_codebase` directory.
  - Response:
    ```json
    {
      "reviews": {
        "file1.py": "<review text>",
        "file2.py": "<review text>"
      }
    }
    ```

---

## Project Structure

```
llama_code_reviewer/
│
├── app/
│   ├── main.py           # (Legacy CLI entry, not used for FastAPI)
│   ├── app_main.py       # FastAPI application
│   ├── utils.py          # File reading utilities
│   └── ollama_agent.py   # Llama code review agent
│
├── test/
│   └── sample_codebase/  # Place your Python files here for batch review
│
├── requirements.txt
└── README.md
```

---

## Notes

- Ensure Ollama is running and the `llama3.1:8b` model is available before starting the FastAPI server. You can check this running the command `ollama list` in the terminal.
- All logs are saved to `app.log` in the project root.
- You can add your Python files to `test/sample_codebase` for batch review via the `/review-all` endpoint at the link [http://localhost:8000/docs](http://localhost:8000/docs).

## Next steps

- The current version may not be suitable for larger code files as the context window of the `llama3.1:8b` model is only 4k tokens.
- Regular chunking techniques may not be suitable for large code files as there could be references to previously defined methods and parameters which might exceed the context window.
- `SemanticChunker` by `LangChain` seems promising to chunk the code with semantic similarity.
- Chunking based on abstract syntax trees (provided by the Python library `ast`) also looks promising for at least the delayed references to previously defined methods.
- Vector database approach is another candidate which can be explored.
