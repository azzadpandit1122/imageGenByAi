# AI Image Generation with Hugging Face and Python

This project demonstrates how to generate images from text descriptions using a pre-trained model hosted on Hugging Face, specifically the **Stable Diffusion** model. Follow the steps below to set up your environment, authenticate, generate images, and display/save them.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Set Up Your Environment](#set-up-your-environment)
3. [Install Required Libraries](#install-required-libraries)
4. [Authenticate with Hugging Face API](#authenticate-with-hugging-face-api)
5. [Load the Pre-trained Model](#load-the-pre-trained-model)
6. [Prepare Your Input (Text Prompt)](#prepare-your-input-text-prompt)
7. [Generate Image from Model](#generate-image-from-model)
8. [Save and Display the Image](#save-and-display-the-image)
9. [Optional: Fine-Tuning the Model](#optional-fine-tuning-the-model)
10. [Conclusion](#conclusion)

---

## Prerequisites

Before starting, you need to ensure the following:

- Python 3.7+ installed.
- A Hugging Face account for API authentication. Create one at [Hugging Face](https://huggingface.co).
- GPU (recommended for faster image generation), but CPU can also work.

---

## Set Up Your Environment

It's recommended to use a virtual environment for managing dependencies:

1. **Create a virtual environment:**

   ```bash
   python -m venv image-gen-env
   ```
   **Activate environment**
   ```image-gen-env\Scripts\activate```
   
## Install Dependencies
**Install all required packages:**
```base
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install diffusers transformers huggingface_hub Pillow accelerate
```
## Get Your Hugging Face API Token

1. Visit: https://huggingface.co/settings/tokens  
2. Click **Create New Token**  
3. Choose **READ** access  
4. Copy the generated token
## Authenticate in Python
```base
from huggingface_hub import login
login("YOUR_HUGGINGFACE_API_TOKEN")
```
## Load the Stable Diffusion Model
```base
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)

pipe.to("cuda")  # remove if using CPU only
```
## Create a Text Prompt
```base
prompt = "A futuristic neon-lit city, cyberpunk style, extremely detailed, 4K"
```
## Generate the Image
```base
image = pipe(prompt).images[0]
```
## Save & Display the Image
```base
image.save("generated_image.png")
image.show()
```
## FULL WORKING SCRIPT (generate.py)
**Save this file as:generate.py**
```base
from diffusers import StableDiffusionPipeline
from huggingface_hub import login
import torch

# --------------------------------------
# 1. Authenticate Hugging Face
# --------------------------------------
login("YOUR_HUGGINGFACE_API_TOKEN")


# --------------------------------------
# 2. Load the Stable Diffusion Model
# --------------------------------------
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)

# Use GPU if available
pipe.to("cuda")


# --------------------------------------
# 3. Your Image Prompt
# --------------------------------------
prompt = "A beautiful magical forest with glowing flowers, fantasy style, ultra detailed"


# --------------------------------------
# 4. Generate the Image
# --------------------------------------
image = pipe(prompt).images[0]


# --------------------------------------
# 5. Save the Image
# --------------------------------------
image.save("generated_image.png")

print("Image successfully generated and saved as generated_image.png")
```
## Run the Script
```base
python generate.py
```
**This will produce:**
```base
generated_image.png
```
## Optional: Enable GPU Acceleration
```base
import torch
print(torch.cuda.is_available())
```
## Optional: Fine-Tuning
**You can fine-tune Stable Diffusion using:**
```base
✔ DreamBooth
✔ LoRA
✔ Textual Inversion
```

## Suggested Prompts
**A photorealistic portrait of a woman, soft natural lighting, 8K, ultra detailed**


---

If you want this turned into a **GitHub repo**, **zip file**, or **multiple scripts**, just tell me!



