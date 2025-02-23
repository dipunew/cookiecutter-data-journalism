# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## 🎯 Workflow
1️⃣ **Set up the project** 🔧  
2️⃣ **Process Data** 🧼 (notebooks/0.0-process.ipynb)  
3️⃣ **Analyze Data** 🔎 (notebooks/1.0-analyze.ipynb)  
4️⃣ **Visualize Data** 📊 (notebooks/2.0-visualize.ipynb)  
5️⃣ **Write a Report** ✏️ (docs/reports)  
6️⃣ **Publish a Story** 👥 (quarto/index.qmd)  

## 📁 Directory Structure

# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## 🎯 Workflow
1️️⃣️⃣️⃣ **Set up the project** 🔧
2️️⃣️⃣️⃣ **Process Data** 🧼 (notebooks/0.0-process.ipynb)
3️️⃣️⃣️⃣ **Analyze Data** 🔎 (notebooks/1.0-analyze.ipynb)
4️️⃣️⃣️⃣ **Visualize Data** 📊 (notebooks/2.0-visualize.ipynb)
5️️⃣️⃣️⃣ **Write a Report** ✏️️  ️ (docs/reports)
6️️⃣️⃣️⃣ **Publish a Story** 👥 (quarto/index.qmd)

## 📁 Directory Structure  ├── data/
│ ├── raw/ # Original data │ ├── processed/ # Cleaned data │ ├── docs/
│ ├── references/ # Papers, manuals, articles │ ├── reports/ # Final reports (PDF, HTML) │ ├── data-dictionary.md # Data description │ ├── explore-data.md # Exploratory analysis notes │ ├── notebooks/
│ ├── 0.0-process.ipynb # Data cleaning │ ├── 1.0-analyze.ipynb # Exploratory data analysis │ ├── 2.0-visualize.ipynb # Data visualization │ ├── outputs/
│ ├── figures/ # Charts and maps │ ├── tables/ # Data tables │ ├── quarto/
│ ├── index.qmd # Main Quarto document │ ├── _quarto.yml # Quarto configuration │ ├── src/ # Python scripts for data analysis │ ├── pyproject.toml # uv dependency management ├── requirements.lock # uv package lock file ├── LICENSE # Project license ├── .gitignore # Ignore unnecessary files └── README.md # Project overview 

---

## **3️⃣ Save and Exit**
Once you have pasted the text, **save and exit nano**:
- **Press `CTRL + X`** to exit the editor.
- **Press `Y`** when it asks if you want to save changes.
- **Press `Enter`** to confirm and return to the terminal.

---

## **4️⃣ Commit Your Changes to Git**
Now that the file is saved, you need to commit and push it to GitHub:

```bash
git add .
git commit -m "Added README.md template"
git push origin main

