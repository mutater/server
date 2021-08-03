from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/magyka")
def magyka():
    return render_template("magyka.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
