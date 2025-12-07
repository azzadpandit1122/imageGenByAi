import os
import subprocess
import sys
import venv
import shutil

# -------------------------------
# Configuration
# -------------------------------
VENV_DIR = ".venv"                  # Name of the virtual environment folder
USE_GPU = False                     # True for GPU version, False for CPU
MODEL_SCRIPT = "download_model.py"  # Your model script

# -------------------------------
# Helper functions
# -------------------------------
def run(cmd):
    """Run a shell command in PowerShell."""
    print(f"\n➡ Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed with code {result.returncode}: {cmd}")
        sys.exit(1)

def delete_broken_venv():
    """Delete venv if it is broken or missing pyvenv.cfg."""
    venv_cfg = os.path.join(VENV_DIR, "pyvenv.cfg")
    if os.path.exists(VENV_DIR) and (not os.path.exists(venv_cfg)):
        print(f"⚠️  Detected broken venv, deleting: {VENV_DIR}")
        try:
            shutil.rmtree(VENV_DIR)
        except PermissionError:
            print("❌ Cannot delete venv while active. Please deactivate and rerun.")
            sys.exit(1)

def create_venv():
    """Create virtual environment."""
    if not os.path.exists(VENV_DIR):
        print(f"✨ Creating virtual environment: {VENV_DIR}")
        venv.create(VENV_DIR, with_pip=True)
    else:
        print(f"⚡ Virtual environment already exists: {VENV_DIR}")

def get_pip_path():
    return os.path.join(VENV_DIR, "Scripts", "pip.exe")

def get_python_path():
    return os.path.join(VENV_DIR, "Scripts", "python.exe")

# -------------------------------
# Main setup process
# -------------------------------
if __name__ == "__main__":
    # Step 1: Delete broken venv if needed
    delete_broken_venv()

    # Step 2: Create venv if missing
    create_venv()

    pip_path = get_pip_path()
    python_path = get_python_path()

    # Step 3: Upgrade pip
    run(f'"{python_path}" -m pip install --upgrade pip')

    # Step 4: Install PyTorch
    if USE_GPU:
        print("⚡ Installing GPU-enabled PyTorch")
        run(f'"{pip_path}" install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121')
    else:
        print("⚡ Installing CPU-only PyTorch")
        run(f'"{pip_path}" install torch --index-url https://download.pytorch.org/whl/cpu')
        run(f'"{pip_path}" install torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu')

    # Step 5: Install other dependencies
    run(f'"{pip_path}" install diffusers transformers accelerate')

    # Step 6: Run your model script
    model_path = os.path.abspath(MODEL_SCRIPT)
    if not os.path.exists(model_path):
        print(f"❌ Model script not found: {model_path}")
        sys.exit(1)

    run(f'"{python_path}" "{model_path}"')

    print("\n✅ Setup complete and model script executed successfully!")
