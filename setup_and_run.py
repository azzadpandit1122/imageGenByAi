import os
import subprocess
import sys
import venv
import shutil

# -------------------------------
# Configuration
# -------------------------------
VENV_DIR = ".venv"                  # Virtual environment folder
FORCE_CPU = True                    # Force CPU-only PyTorch to avoid WinError 1114
MODEL_SCRIPT = "download_model.py"  # Your model script
PYTORCH_CUDA_INDEX = "cu121"        # GPU version if FORCE_CPU=False

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
    if os.path.exists(VENV_DIR) and not os.path.exists(venv_cfg):
        print(f"⚠️  Detected broken venv, deleting: {VENV_DIR}")
        try:
            shutil.rmtree(VENV_DIR)
        except PermissionError:
            print("❌ Cannot delete venv while active. Please deactivate and rerun.")
            sys.exit(1)

def create_venv():
    """Create virtual environment if missing."""
    if not os.path.exists(VENV_DIR):
        print(f"✨ Creating virtual environment: {VENV_DIR}")
        venv.create(VENV_DIR, with_pip=True)
    else:
        print(f"⚡ Virtual environment already exists: {VENV_DIR}")

def get_pip_path():
    return os.path.join(VENV_DIR, "Scripts", "pip.exe")

def get_python_path():
    return os.path.join(VENV_DIR, "Scripts", "python.exe")

def install_dependencies(pip_path):
    """Install PyTorch and other dependencies."""
    if FORCE_CPU:
        print("⚡ Installing CPU-only PyTorch")
        run(f'"{pip_path}" install --upgrade pip')
        run(f'"{pip_path}" install torch --index-url https://download.pytorch.org/whl/cpu')
        run(f'"{pip_path}" install torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu')
    else:
        print(f"⚡ Installing GPU-enabled PyTorch ({PYTORCH_CUDA_INDEX})")
        run(f'"{pip_path}" install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/{PYTORCH_CUDA_INDEX}')

    # Install diffusers, transformers, accelerate
    run(f'"{pip_path}" install diffusers transformers accelerate')

# -------------------------------
# Main setup and execution
# -------------------------------
if __name__ == "__main__":
    # Step 1: Delete broken venv if exists
    delete_broken_venv()

    # Step 2: Create virtual environment
    create_venv()

    pip_path = get_pip_path()
    python_path = get_python_path()

    # Step 3: Upgrade pip
    run(f'"{python_path}" -m pip install --upgrade pip')

    # Step 4: Install dependencies
    install_dependencies(pip_path)

    # Step 5: Force CPU-only for torch
    os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Ensures CPU-only execution

    # Step 6: Run the model script
    model_path = os.path.abspath(MODEL_SCRIPT)
    if not os.path.exists(model_path):
        print(f"❌ Model script not found: {model_path}")
        sys.exit(1)

    # Run the model in the new environment
    run(f'"{python_path}" "{model_path}"')

    print("\n✅ Production setup complete and model executed successfully!")
