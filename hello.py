from flask import Flask
app = Flask(__name__)

@app.route("/")
ddef salvador():
    return 'Hello World!'
