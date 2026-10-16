import tomllib
from pathlib import Path

# Load the file path
pyproject_path = Path("pyproject.toml")

# Read and parse the TOML file
with open(pyproject_path, "rb") as f:
    config = tomllib.load(f)

version = config.get("project", {}).get("version")
