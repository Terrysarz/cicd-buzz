from flask import Flask
from buzz.generator import generate_buzz

app = Flask(__name__)


@app.route('/')
def hello():
    return generate_buzz()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
