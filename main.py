import json
import random

import gradio as gr

from intermediate import intermediate
from websockets_api import get_prompt_image
from advanced import advance

def process(positive):
    with open("txt2img.json", "r", encoding="utf-8") as f:
        prompt = json.load(f)
    prompt["6"]["inputs"]["text"] = "a half portrait of a" + positive + "highly detail, high resolution"
    prompt["3"]["inputs"]["seed"] = random.randint(0, 99999999999)

    images = get_prompt_image(prompt)
    return images


basic = gr.Interface(
    fn=process,
    inputs=[gr.Textbox(label="Positive Prompt: ")],
    outputs=[gr.Gallery(label="Outputs: ")]
)

demo = gr.TabbedInterface(interface_list=[basic, intermediate, advance],
                          tab_names=["Basic Workflow", "Intermediate Workflow", "Advanced Workflow"])

demo.queue()
demo.launch()
