from diffusers import StableDiffusionPipeline
import torch
import os

LOCAL_DIR = "./models/ghibli-diffusion"
os.makedirs(LOCAL_DIR, exist_ok=True)

print("Downloading Diffusers model from HuggingFace...")

pipe = StableDiffusionPipeline.from_pretrained(
    "nitrosocke/Ghibli-Diffusion",
    torch_dtype=torch.float32  # CPU uses float32
)

pipe.save_pretrained(LOCAL_DIR)

print("Model downloaded and saved to:", LOCAL_DIR)
