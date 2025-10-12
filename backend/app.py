from flask import Flask, render_template, request, send_file, jsonify
from utils.doc_generator import generate_resume
import os

# Serve frontend from frontend/ folder
app = Flask(__name__, template_folder="../frontend", static_folder="../frontend")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate-resume', methods=['POST'])
def generate_resume_endpoint():
    try:
        data = request.get_json()
        filepath = generate_resume(data)
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# ------------------ PROMPT FUNCTION ------------------
def build_resume_prompt(form_data):
    """
    Converts form JSON data into a structured prompt for Perplexity Pro API.
    """
    prompt = f"""
You are an expert resume writer. Create a professional, ATS-friendly resume
using the following candidate information.

Name: {form_data.get('name')}
Email: {form_data.get('email')}
Role Applied For: {form_data.get('role')}

Professional Summary (if provided):
{form_data.get('summary', 'N/A')}

Skills:
{', '.join(form_data.get('skills', []))}

Education:
{form_data.get('education', 'N/A')}

Work Experience:
"""
    for exp in form_data.get('experience', []):
        prompt += f"""
- Company: {exp.get('company')}
  Role: {exp.get('role')}
  Duration: {exp.get('years')}
  Details: {exp.get('details')}
"""

    prompt += """

Instructions for output:
1. Write a 2–3 sentence professional summary at the top.
2. Rewrite work experience in concise, impactful bullet points.
3. Highlight key achievements.
4. Avoid filler words and generic phrases.
5. Format for a professional resume suitable for ATS systems.
"""
    return prompt.strip()

@app.route('/generate_resume_text', methods=['POST'])
def generate_resume_text():
    form_data = request.json  # form sends JSON
    prompt = build_resume_prompt(form_data)
    
    # Placeholder for Perplexity API call
    # resume_text = call_perplexity_api(prompt)
    
    return jsonify({"prompt": prompt})  # for now, just return the prompt


if __name__ == "__main__":
    app.run(debug=True)
    
