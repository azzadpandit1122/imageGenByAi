from diffusers import StableDiffusionPipeline
import torch

MODEL_DIR = "./models/ghibli-diffusion"

print("Loading local Ghibli model...")

# CPU version (float32)
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_DIR,
    torch_dtype=torch.float32
)

# Use CPU only
pipe.to("cpu")

print("Model loaded! Generating...")

prompt = "A peaceful lakeside village with glowing lanterns in Studio Ghibli art style"

image = pipe(prompt).images[0]

output_path = "ghibli_output.png"
image.save(output_path)

print("Image saved as:", output_path)
