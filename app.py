import gradio as gr
from groq import Groq
from src.utils.prompts import SYSTEM_PROMPT, EXAMPLE_QUESTIONS
from src.config.settings import GROQ_API_KEY, CHATBOT_NAME

def get_groq_client():
    """Initialize and return Groq client"""
    api_key = GROQ_API_KEY
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")
    return Groq(api_key=api_key)

client = get_groq_client()

def respond(message, history, model, temperature, max_tokens):
    """
    Generate streaming response from Instructor for Agentic AI
    
    Args:
        message: User's current question
        history: List of previous chat messages (Gradio format)
        model: Selected AI model
        temperature: Temperature parameter for response randomness
        max_tokens: Maximum tokens for response length
    
    Returns:
        Generator yielding response chunks
    """
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    if history:
        for chat in history:
            if isinstance(chat, (list, tuple)) and len(chat) >= 2:
                user_msg, assistant_msg = chat[0], chat[1]
                if user_msg:
                    messages.append({"role": "user", "content": str(user_msg)})
                if assistant_msg:
                    messages.append({"role": "assistant", "content": str(assistant_msg)})
    
    messages.append({"role": "user", "content": message})
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=int(max_tokens),
            stream=True
        )
        
        response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                response += chunk.choices[0].delta.content
                yield response
                
    except Exception as e:
        yield f"Error: {str(e)}"

app = gr.ChatInterface(
    fn=respond,
    title=f"🧭 {CHATBOT_NAME}",
    description=f"Ask questions about designing, building, and refining agentic AI systems with {CHATBOT_NAME}.",
    additional_inputs=[
        gr.Dropdown(
            choices=[
                "qwen/qwen3-32b",
                "moonshotai/kimi-k2-instruct",
                "moonshotai/kimi-k2-instruct-0905",
            ],
            value="qwen/qwen3-32b",
            label="Model",
            info="Select the AI model to use"
        ),
        gr.Slider(
            minimum=0,
            maximum=2,
            value=0.9,
            step=0.1,
            label="Temperature",
            info="Controls randomness. Lower = more focused, Higher = more creative"
        ),
        gr.Slider(
            minimum=256,
            maximum=8192,
            value=2048,
            step=256,
            label="Max Tokens",
            info="Maximum length of the response"
        ),
    ],
    examples=EXAMPLE_QUESTIONS,
)

if __name__ == "__main__":
    app.launch(share=True)