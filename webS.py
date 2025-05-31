import os
from flask import Flask , render_template
from student_data import te_dhenat_e_studenteve

app = Flask(__name__)

def merr_Studentet():
    folder = "data"
    if not os.path.exists(folder):
        return []
    files = os.listdir(folder)
    return [file.replace(".json", "") for file in files if file.endswith(".json")]

@app.route("/")
def home():
    studentet = merr_Studentet()
    return render_template("home.html", studentet = studentet)

@app.route("/studenti/<username>")
def faqja_studentit(username):
    data = te_dhenat_e_studenteve(username)
    kurset = data.get("Kurset", {})
    rekomandimi = data.get("Rekomandimet", {})
    return render_template("student.html", username = username, kurset= kurset, rekomandimi = rekomandimi)


#python -m flask --app webS.py run