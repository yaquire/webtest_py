from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<who>")
def hello(who):
    return render_template("greet.html", name=who)


@app.route("/page2")
def page2():
    return "Second Page"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
