# Resume Builder for B.Tech Freshers

An **ATS-friendly resume builder** web application for B.Tech fresh graduates.  
This project allows students to input their academic, technical, and project details via a web form and generates a professional Word resume.

---

## Features

- Collects student data via an HTML form:
  - Personal details
  - Education
  - Skills
  - Trainings & Workshops
  - Projects
- Generates an ATS-friendly Word document (`.docx`)
- Saves resumes in `generated_resumes/` folder
- File names include student name and timestamp to prevent overwriting
- Ready for Campus Placement usage

---

## Folder Structure

resume_builder/
│── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── utils/doc_generator.py
│
│── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
│── generated_resumes/ # Contains generated Word resumes
│
│── .gitignore
│── README.md



---

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/ksrikanthai-create/resume_builder.git

## Install dependencies

pip install -r backend/requirements.txt

## Run the app

## python backend/app.py

## Open frontend/index.html in a browser to use the form.