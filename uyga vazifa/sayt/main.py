from flask import Flask, render_template, request
from parse import mmm

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", fakts = mmm(request.args.get("q")))
    return render_template("index.html", fakts = [])


if __name__ == "__main__":
    app.run(debug=True)