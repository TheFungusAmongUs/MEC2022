from flask import Flask, render_template, request

app = Flask(__name__)


def read_power_level():
    pass


@app.route("/", methods=["GET", "POST"])
async def home():
    if request.method == "POST":
        print(request.form["submit_button"])

    return render_template("index.html")


# a change
@app.route("/logs")
async def logs_page():
    return "Here are the logs:"


@app.route("/test", methods=["GET", "POST"])
async def test_page():
    if request.method == "POST":
        print("HELLO")
    else:
        return render_template("test.html")


@app.route("/settings")
async def settings_page():
    return "settings"


@app.route("/predict", methods=["GET", "POST"])
async def predict_page():
    if request.method == "POST":
        return "Data"
    else:
        return render_template("predictions.html")
