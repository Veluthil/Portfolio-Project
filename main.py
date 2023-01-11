from flask import Flask, render_template, redirect, url_for, flash, request, abort


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/header")
def header():
    return render_template("header.html")


@app.route("/footer")
def footer():
    return render_template("footer.html")


if __name__ == "__main__":
    app.run(debug=True)