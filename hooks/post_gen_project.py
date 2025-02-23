import os

# Define the directory structure
DIRS = [
    "data",
    "data/raw",
    "data/clean",
    "data/processed",
    "docs",
    "docs/references",
    "docs/reports",
    "get_data",
    "notebooks",
    "outputs",
    "outputs/figures",
    "outputs/tables",
    "quarto",
    "src"
]

# Create directories
for dir_path in DIRS:
    os.makedirs(dir_path, exist_ok=True)

# Create essential files
FILES = [
    "README.md",
    ".gitignore",
    "LICENSE",
    "pyproject.toml",
    "requirements.lock"
]

for file in FILES:
    with open(file, "w") as f:
        f.write("")

  
