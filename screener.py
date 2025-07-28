import os, json, re
import pandas as pd
from docx import Document
from PyPDF2 import PdfReader

# Load job criteria
with open("job_criteria.json") as f:
    criteria = json.load(f)

def extract_text(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""

def calculate_score(text):
    text_lower = text.lower()
    score = 0
    matched_skills = []

    # Skill Matching
    for skill in criteria['required_skills']:
        if skill.lower() in text_lower:
            score += 10
            matched_skills.append(skill)

    for bonus in criteria['bonus_skills']:
        if bonus.lower() in text_lower:
            score += 5

    # Experience Scoring
    experience_years = re.findall(r'(\d+)\s+years?', text_lower)
    max_exp = max([int(y) for y in experience_years], default=0)
    if max_exp >= criteria['min_experience']:
        score += max_exp * 2

    return score, matched_skills, max_exp

# Process resumes
results = []
for filename in os.listdir("resumes"):
    path = os.path.join("resumes", filename)
    text = extract_text(path)
    score, skills, exp = calculate_score(text)
    results.append({"Name": filename, "Score": score, "Skills Matched": skills, "Experience (Years)": exp})

# Rank and save
df = pd.DataFrame(results).sort_values(by="Score", ascending=False)
df.to_csv("results.csv", index=False)
print(df)
