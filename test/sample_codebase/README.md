
# Sample Python Codebase for LLM Security Review Testing

This repository contains intentionally vulnerable Python code designed to test the performance of local LLMs like CodeLlama when reviewing for:

- Hardcoded secrets
- Weak or misleading variable names
- Cross-file credential handling
- Common security misconfigurations

Files include:
- `app.py`: Main application logic
- `utils.py`: Input cleaning and data processing
- `config.py`: Contains hardcoded config variables
- `database.py`: Simulates a DB connection using values from config
