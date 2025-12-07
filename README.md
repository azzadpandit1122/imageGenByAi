# 🖼️ AI Image Generation (Stable Diffusion – Python)

A clean, simple, and production-ready Python project for generating images from text prompts using **Stable Diffusion** via Hugging Face.  
This project includes automated setup scripts, model downloading, and image generation with GPU/CPU fallback.

---

## 📁 Project Structure
```cmd
imageGenByAi/
│── .venv/ # Virtual environment (ignored in Git)
│── models/ # Downloaded ML models (ignored in Git)
│── main.py # Main script to generate images
│── download_model.py # Script to download Stable Diffusion model
│── setup_and_run.py # One-click setup + run helper
│── .gitignore
│── README.md
```

---

## 🚀 Features

- Generate images using Stable Diffusion  
- Automatic GPU or CPU use  
- Download model once → stored in `models/`  
- Clean scripts for setup and inference  
- 100% reproducible environment setup  

---

## 🛠️ Requirements

- **Python 3.10**
- Hugging Face account  
- Optional: NVIDIA GPU (recommended for faster generation)

---

## ⚙️ Setup Instructions

### 1️⃣ Create & Activate Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\activate

- If you want GPU acceleration (CUDA 12.1):
```cmd 
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
- Install remaining libraries:
```cmd
pip install diffusers transformers huggingface_hub pillow accelerate
```

## Hugging Face Authentication

- Visit: https://huggingface.co/settings/tokens
- Click Create New Token → set to READ
- Use the token in scripts:

## Download the Model
- Run the included script:
python download_model.py

- This downloads the Stable Diffusion model into:
models/

## Generate an Image
```cmd 
python main.py
```
- Example prompt inside main.py:
```cmd 
prompt = "A futuristic neon-lit city, cyberpunk style, extremely detailed, 4K"
```
## One-Click Setup + Run
```cmd
python setup_and_run.py
```

📣 Contributions & Issues
Feel free to open issues or request improvements for scripts, prompts, or better GPU utilization.


---

If you want a **GitHub-optimized version with badges, screenshots, or installation GIF**, I can generate that too!
