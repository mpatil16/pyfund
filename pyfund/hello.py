from flask import Flask
app = Flask(__name__)

@app.route("/hello1")
def hello():
    return "Hello Mahesh!"

if __name__ == "__main__":
    app.run()