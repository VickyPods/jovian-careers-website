from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)


JOBS =[
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bangaluru',
        'salary': 'Rs. 1,00,000'

    },
     {
        'id': 2,
        'title': 'Devops Engineer',
        'location': 'Bangaluru',
        'salary': 'Rs. 2,00,000'

    },
     {
        'id': 3,
        'title': 'Full stack Engineer',
        'location': 'Bangaluru',
        # 'salary': 'Rs. 2,00,000'

    }
]

@app.route('/')
def hello_world():
    return render_template("home.html", jobs =JOBS, company_name= "Jovian")


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True,host= "0.0.0.0", port=8089)