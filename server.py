# coding = utf-8
from flask import Flask


__author__ = "Zeinab Abbasimazar"


app = Flask(__name__)


@app.route("/")
def home():
    pass


if __name__ == "__main__":
    app.run("0.0.0.0", debug=False)
