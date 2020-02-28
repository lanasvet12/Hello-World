from flask import Flask
app = Flask(__name__)

@app.route("/")
def salvador():
    return 'Hello World!'
