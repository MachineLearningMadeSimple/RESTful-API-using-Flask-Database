from flask import Flask, jsonify, request

app = Flask(__name__)

database = [
    {
        "student_id": ["10091203"],
        "first_name": ["Samuel"],
        "last_name": ["L.Jackson"],
        "dob": ["April 1st"],
        "amount_due": ["40000"]
    },
    {
        "student_id": ["100678192"],
        "first_name": ["Jim"],
        "last_name": ["Halpert"],
        "dob": ["October 15th"],
        "amount_due": ["891900"]
    },
    {
        "student_id": ["10078390"],
        "first_name": ["Pamm"],
        "last_name": ["Beasly"],
        "dob": ["May 4th"],
        "amount_due": ["250000"]
    }
]

@app.route("/database")
def hello():
    return jsonify(database)


app.run()
