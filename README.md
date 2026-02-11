---
title: Instructor For Agentic Ai
emoji: 🦀
colorFrom: pink
colorTo: red
sdk: gradio
sdk_version: 6.5.1
app_file: app.py
pinned: false
short_description: AI-powered Instructor for Agentic AI using Groq and Gradio
---

# Instructor for Agentic AI

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Clone from GitHub](#clone-from-github)
  - [Conda environment](#conda-environment)
  - [Run locally](#run-locally)
  - [Duplicate Hugging Face Space](#duplicate-hugging-face-space)
- [Contributing](#contributing)
- [Author](#author)

## Overview
AI-powered Instructor for Agentic AI using Groq API and Gradio.

## Project Structure
```
agentic-instructor-chatbot
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .gitattributes
├── .env
├── research/
│   └── notebook.ipynb
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





## Project Structure
```
web-search/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .gitattributes
├── .env
├── research/
│   └── notebook.ipynb
└── src/
    ├── __init__.py
    ├── config/
    │   ├── __init__.py
    │   └── settings.py
    └── utils/
        ├── __init__.py
        └── chat.py
```

## Setup

- GitHub repo: [link](https://github.com/elsayedelmandoh/web-search)
- Hugging Face Space: [link](https://huggingface.co/spaces/elsayedelmandoh/Gemini_3_Web_Search)

### Clone from GitHub
```bash
git clone https://github.com/elsayedelmandoh/web-search
cd web-search
```

### Conda environment
```bash
# create & activate
conda create -n web-search python=3.12 -y
conda activate web-search

# install pip then dependencies
conda install pip -y
pip install -r requirements.txt
```
You may use a .env loader or store vars in the Hugging Face Space secrets.

### Run locally
```bash
python app.py
```
Open the URL printed in the terminal.

### Duplicate Hugging Face Space

Hugging Face Space URL used in this project:
https://huggingface.co/spaces/elsayedelmandoh/Gemini_3_Web_Search

1. Sign in to Hugging Face.
2. Go to the Space you want to duplicate.
3. Click the "Duplicate this Space" button.
4. Choose a new name and visibility, then Duplicate Space.
5. In the new Space settings add secrets (GEMINI_API_KEY) and push code.

## Contributing
1. Fork the repository.
2. Create a branch for your change.
3. Make changes, commit with clear messages.
4. Push to your fork and open a pull request.

## Author
Developed by Elsayed Elmandoh — NLP Engineer.  
LinkedIn: https://linkedin.com/in/elsayed-elmandoh-b5849a1b8/  
X/Twitter: https://x.com/aangpy
