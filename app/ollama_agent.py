import ollama
import logging

logger = logging.getLogger(__name__)

class LlamaCodeReviewAgent:
    def __init__(self, model_name: str = "llama3.1:8b"):
        self.model_name = model_name

    def review_code(self, filename: str, code: str) -> str:
        prompt = f"""
        You are a professional code reviewer.

        Review the following Python file for the following aspects:
        1. Hardcoded sensitive information (API keys, passwords, IPs, tokens)
        2. Non-contextual or misleading variable names
        3. Possible database credentials or configuration leaks

        Please follow this format exactly, without adding or removing any sections.

        ---

        **Filename:** {filename}

        **Code Quality Rating:** [1-10]

        **Findings:**
        - **Sensitive Info:** <Write “None found” or a bullet list of issues>
        - **Bad Variable Names:** <Write “None found” or a bullet list of bad variable names with suggestions>
        - **Credential Leaks:** <Write “None found” or a bullet list of suspicious credentials or config leaks>

        **Overall Comments:**
        <Write a brief and insightful summary of the overall code quality, in 2-3 sentences.>

        ---

        Review the following Python code:

        ```python
        {code}
        """
        response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]