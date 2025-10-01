import datetime
from utils.doc_generator import generate_resume

if __name__ == "__main__":
    # Example student data
    student_data = {
        "name": "John Student",
        "contact": {
            "phone": "+91-9876543210",
            "email": "john.student@example.com",
            "linkedin": "linkedin.com/in/johnstudent",
            "github": "github.com/johnstudent"
        },
        "summary": "Enthusiastic B.Tech graduate in AI & DS with strong coding skills in Python and SQL. Passionate about data engineering and cloud technologies. Seeking opportunities to apply problem-solving skills in real-world projects.",
        
        "education": [
            {"degree": "B.Tech in AI & DS", "institution": "XYZ College", "year": "2025"},
            {"degree": "Intermediate", "institution": "ABC Junior College", "year": "2021"}
        ],
        
        "skills": ["Python", "SQL", "Machine Learning", "Data Engineering"],
        
        "training": [
            {"title": "Workshop on Cloud Services for Data Engineering", "from": "5th June 2025", "to": "15th June 2025"}
        ],
        
        "projects": [
            {"name": "Student Feedback Portal", "description": "A web app for collecting and analyzing student feedback"}
        ],
        
        "certifications": [
            {"title": "AWS Cloud Practitioner", "year": "2024"},
            {"title": "Azure Fundamentals", "year": "2023"}
        ],
        
        "achievements": [
            "Winner of Coding Hackathon 2023 at XYZ College",
            "Secured 2nd place in State-level Math Olympiad"
        ],
        
        "extracurricular": [
            "Member of AI Club at college",
            "Organized Tech Fest 2023"
        ]
        }


        # Generate resume
    filename = generate_resume(student_data)
    print(f"Resume generated: {filename}")
