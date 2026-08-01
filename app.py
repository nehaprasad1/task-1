import random
import os
import csv
from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
names = ["Neha Prasad", "Bob The-Builder", "ABC Xyx", "ASS Pass", "Jhone sinha"]
crs = ["Intro to Python", "Advanced Python", "Web Development", "Data Science"]


@app.route('/api/certificates', methods=['GET'])
def get_certificates():
    student = {
        "id": random.randint(1000, 9999),
        "name": random.choice(names),
        "course": random.choice(crs),
        "date": "2026-07-21"
    }
    
    import io
    
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=student.keys())
    writer.writeheader()
    writer.writerow(student)


    return Response(output.getvalue(), mimetype="text/csv")

if __name__ == '__main__':

    app.run(debug=True)