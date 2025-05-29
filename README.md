# OCI GenAI Agent Python Project

This project is a modular Python agent framework featuring:
- Conversational CLI chat with Google Gemini LLM
- Tool support: DuckDuckGo search, current date, OCI CLI command execution
- Easy extensibility for new tools

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── main.py
│   └── tools/
│       ├── __init__.py
│       ├── current_date.py
│       ├── duckduckgo_search.py
│       └── oci_cli.py
└── tests/
    └── test_main.py
```

## Setup

1. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
   - For DuckDuckGo: No API key needed.
   - For Current Weather (if you add it): Set `OPENWEATHER_API_KEY`.
   - For OCI CLI tool: Ensure `oci` CLI is installed and configured (`oci setup config`).
   - For Gemini: Set up your Google API key if required by your environment.

## Features

### 1. Conversational CLI Chat
- Run the CLI chat interface:
  ```bash
  python src/main.py
  ```
- Type your questions. The agent can:
  - Answer general questions using Gemini LLM
  - Search the web using DuckDuckGo
  - Provide the current date
  - Run OCI CLI commands (e.g., `oci os ns get`)
- Type `exit` or `quit` to leave the chat.

### 2. Modular Tool Support
- Tools are defined in `src/tools/` and imported in `main.py`.
- Add new tools by creating a new file in `src/tools/` and exposing it in `__init__.py`.

## Running Tests

To run the tests:
```bash
pytest
```

## Notes
- The OCI CLI tool will execute commands on your system. Use with caution.
- Make sure your environment variables and API keys are set as needed for all features. 