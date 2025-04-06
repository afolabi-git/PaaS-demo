from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "This is a Demomstration of PaaS. This is a miniproject executed at Darey.io"
