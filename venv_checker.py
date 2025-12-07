# venv_checker.py
import sys

class VenvChecker:
    """Class to check if a virtual environment is active and prompt user if not."""

    @staticmethod
    def is_venv_active():
        return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

    @staticmethod
    def ensure_venv():
        if VenvChecker.is_venv_active():
            print(f"✅ Virtual environment is already active: {sys.prefix}")
        else:
            print("⚠️ Virtual environment is NOT activated.")
            print("Please activate your virtual environment and press Enter to continue...")
            input()  # wait for user to activate and hit Enter
            if VenvChecker.is_venv_active():
                print(f"✅ Virtual environment activated: {sys.prefix}")
            else:
                print("❌ Still not activated. Exiting.")
                sys.exit(1)
