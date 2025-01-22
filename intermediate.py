import json
import random

import gradio as gr
from websockets_api import get_prompt_image
from pathlib import Path
from PIL import Image
from settings import COMFY_UI_PATH


def save_input_image(img):
    input_img = Path(COMFY_UI_PATH) / 'input/intermediate_style_image.jpg'
    pillow_image = Image.fromarray(img)
    pillow_image.save(input_img)

def process(positive, img, slider):
    with open("intermediate_workflow.json", "r", encoding="utf-8") as f:
        prompt = json.load(f)
    prompt["6"]["inputs"]["text"] = "a half portrait of a" + positive + "highly detail, high resolution"
    prompt["3"]["inputs"]["seed"] = random.randint(0, 99999999999)
    prompt["13"]["inputs"]["weight"] = slider

    save_input_image(img)
    images = get_prompt_image(prompt)
    return images


intermediate = gr.Interface(
    fn=process,
    inputs=[gr.Textbox(label="Positive Prompt: "),
            gr.Image(label="Style Image"),
            gr.Slider(label="Image Weight", minimum=0.0, maximum=1.0, step=0.05)
            ],
    outputs=[gr.Gallery(label="Outputs: ")]
)
