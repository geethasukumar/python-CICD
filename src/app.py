from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to DXC - CI/CD Actions!"


if __name__ == "__main__":
    app.run()