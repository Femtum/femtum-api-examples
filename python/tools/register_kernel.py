"""
Register a Jupyter kernel for this Poetry project.

This script creates an IPython kernel that uses the Poetry virtual environment,
allowing notebooks to access all installed dependencies.
"""

import subprocess
import sys
from pathlib import Path


def main():
    # Get the project root (where pyproject.toml lives)
    project_root = Path(__file__).parent.parent
    project_name = project_root.name

    # Install the kernel spec pointing to this venv's Python
    print(f"Registering Jupyter kernel for '{project_name}'...")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "ipykernel",
            "install",
            "--user",
            "--name",
            project_name,
            "--display-name",
            f"Python ({project_name})",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print(f"✓ Kernel '{project_name}' registered successfully!")
        print(f"  Display name: Python ({project_name})")
        print("\nYou can now select this kernel in Jupyter/VS Code.")
    else:
        print(f"✗ Failed to register kernel:")
        print(result.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
