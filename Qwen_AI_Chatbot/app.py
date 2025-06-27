import gradio as gr
import ollama

# Function to interact with the Qwen2.5 Model Chatbot
def qwen_chatbot(message):
    response = ollama.chat(
        model='qwen2.5',
        messages=[{'role': 'user', 'content': message}]
    )
    return response['message']['content']  # Extract only the string part

# Build a Gradio interface
chatbot_ui = gr.Interface(
    fn=qwen_chatbot,
    inputs=gr.Textbox(label="📝 Enter Your Message Here"),
    outputs=gr.Textbox(label="📘 Bot Response "),
    title="🤖 AI-Powered Chatbot",
    description="Chat with an AI Chatbot powered by Qwen 2.5 and Ollama.",
    examples=[
        ["What is your Name?"],
        ["Hi, How are you?"],
        ["What is AI?"],
        ["Where is India?"]
    ],
    theme="ocean" # Options : ocean, glass, soft, origin
)

# Launch the app
if __name__ == "__main__":
    chatbot_ui.launch(show_error=True)
