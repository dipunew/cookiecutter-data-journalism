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

# Define Jupyter Notebooks
NOTEBOOKS = {
    "notebooks/0.0-get-data.ipynb": "# 0.0 Get Data\n\nCollect data from web, files, or database.",
    "notebooks/0.1-clean-data.ipynb": "# 0.1 Clean Data\n\nFix types, remove nulls, clean messy data.",
    "notebooks/0.2-process.ipynb": "# 0.2 Process Data\n\nFurther wrangle data for quality analysis.",
    "notebooks/1.0-analyze.ipynb": "# 1.0 Analyze Data\n\nFind patterns and relationships.",
    "notebooks/2.0-visualize.ipynb": "# 2.0 Visualize Data\n\nCreate charts, graphs, and maps."
}

# Define Markdown files
MARKDOWN_FILES = {
    "docs/data-dictionary.md": "# Data Dictionary\n\nExplain dataset columns and metadata.",
    "docs/explore-data.md": "# Explore Data\n\nInterrogate dataset context and ask questions."
}

# Define essential project files
FILES = [
    "README.md",
    ".gitignore",
    "LICENSE",
    "pyproject.toml",
    "requirements.lock"
]

# Create Jupyter Notebooks with placeholders
for notebook, content in NOTEBOOKS.items():
    with open(notebook, "w") as f:
        f.write(content)

# Create Markdown files with placeholders
for markdown, content in MARKDOWN_FILES.items():
    with open(markdown, "w") as f:
        f.write(content)

# Create essential empty project files
for file in FILES:
    with open(file, "w") as f:
        f.write("")

