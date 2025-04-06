from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "This is a Demomstration of PaaS\n This project was done at Darey.io"
