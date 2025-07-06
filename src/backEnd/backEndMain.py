import os
from flask import Flask

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    print("starting the backend sever")
    app = Flask(__name__)