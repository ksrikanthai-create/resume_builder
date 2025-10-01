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

if __name__ == "__main__":
    app.run(debug=True)
