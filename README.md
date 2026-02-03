# Instructor for Agentic AI

Queens University - GenAI - From Studio 2, Lab 1: Building a custom LLM Chatbot.   
AI-powered Instructor for Agentic AI using Groq API and Gradio.

## Project Structure

```
agentic-instructor-chatbot
├── src
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   └── utils
│       ├── __init__.py
│       └── prompts.py
├── .env
├── .gitignore
├── requirements.txt
├── notebook.ipynb
├── app.py
└── README.md
```

## Features

- Agentic instruction generation: Produces step-by-step, actionable instructor responses tailored for agentic tasks and workflows.
- Groq-powered LLM integration: Uses the Groq API to run performant LLM calls with configurable prompts and context handling.
- Interactive Gradio UI: A lightweight Gradio interface for live conversations, iteration on prompts, and rapid feedback.

## Installation


1. Clone the repository:
   ```
   git clone https://github.com/elsayedelmandoh/instructor-for-agentic-ai
   cd instructor-for-agentic-ai
   ```

2. Create a development environment (Linux + Conda):

   - Using `conda` (recommended):

   ```bash
   # create a new conda environment with a supported Python version
   conda create -n agentic-instructor python=3.12 -y

   # activate the environment
   conda activate agentic-instructor

   # install dependencies
   pip install -r requirements.txt
   ```

   - If you prefer a plain virtualenv on Linux (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. To run the chatbot, execute the following command:
```
python app.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
