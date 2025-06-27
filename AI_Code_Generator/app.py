import gradio as gr
import ollama

# Function to generate code from prompt
def generate_code(prompt):
    response = ollama.chat(
        model='qwen2.5-coder',
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']  # Extract only the string part

# Gradio UI
interface = gr.Interface(
    fn=generate_code,
    inputs=gr.Textbox(label="💬 Describe the Code You Need", placeholder="e.g., Create a Python function to sort a list"),
    outputs=gr.Code(label="🧠 Generated Code", language="python"),
    title="💻 AI Code Generator",
    description="Powered by Qwen2.5-coder Model with Ollama. Generate Python code from Natural Language.",
    theme="glass",
    examples=[
        ["Create a Function to check if a number is prime"],
        ["Reverse a String in Python"],
        ["Generate a Function to check leap year"],
    ]
)

# Launch the app
interface.launch()
