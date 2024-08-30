
import gradio as gr
from test import get_message_content


demo = gr.Interface(
    fn=get_message_content,
    inputs=["text"],
    outputs=["text"],
)

demo.launch()
