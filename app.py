from flask import Flask

app = Flask(__name__)

@app.route("/")
def run():
    return "{\"messege\":\"Hey there python\"}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)