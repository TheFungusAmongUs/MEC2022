from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
async def home():
    if request.method == "POST":
        print("TESTING")
        print(request.form.getlist("test state"))
    return render_template("index.html")


# a change
@app.route("/logs")
async def logs_page():
    return "Here are the logs:"


@app.route("/test", methods=["GET", "POST"])
async def test_page():
    if request.method == "POST":
        print("HELLO")
        print(request.form.getlist("test state"))
    else:
        return url_for('test_page')


@app.route("/settings")
async def settings_page():
    return "settings"


@app.route("/predict")
async def predict_page():
    return "predictions!!!"
