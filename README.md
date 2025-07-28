# 🧾 Resume Screener (Python CLI Project)

## 📌 Overview

Resume Screener is a Python-based Command Line Interface (CLI) tool that helps filter out candidate resumes based on a predefined set of skills and keywords. This project simulates a basic HR task where the system reads through multiple resume files and highlights those that match specific hiring criteria.

---

## 🚀 Features

- Reads resume files (`.txt` format) from a folder.
- Loads screening criteria from a JSON file.
- Matches keywords case-insensitively.
- Displays shortlisted resumes with matched keywords.
- Clean CLI output for easy understanding.

---

## 🛠️ Technologies & Libraries Used

- **Python 3.x**
- `os` – for handling files and directories
- `json` – to read screening criteria
- `colorama` – to add color to CLI output
- `re` – for pattern and keyword matching

---

## 📂 Folder Structure
resume_screener/
│
├── resumes/ # Folder containing candidate resume text files
│ ├── resume1.txt
│ └── resume2.txt
│
├── criteria.json # JSON file with list of required skills/keywords
├── screener.py # Main Python script
└── README.md # Project documentation


---

## 🧠 How It Works

1. **Setup** your resumes inside the `resumes/` folder.
2. Define your desired keywords in `criteria.json`, like:
   ```json
   ["python", "sql", "data analysis"]
