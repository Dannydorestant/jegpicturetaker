from flask import Flask, redirect,url_for,render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("pics.html")


if __name__ == "__main__":
    app.run(host="192.168.1.243")
