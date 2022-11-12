from flask import Flask, render_template, request
import csv
import datetime
from engcomp import Predictor


app = Flask(__name__)


with open("testing/our_data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    weather_data = list(reader)
    for row in weather_data:
        row["Date time"] = datetime.datetime.fromisoformat(row["Date time"])


def read_power_level():
    pass


test_status: bool = False


@app.route("/", methods=["GET", "POST"])
async def home():
    global test_status
    if request.method == "POST":
        print(request.form["submit_button"])
        test_status = not test_status
    return render_template("index.html", test_status=str(test_status))


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



def get_closest_time(date_time):
    best_delta = datetime.timedelta(10000000)
    best_date_time = None
    for data in weather_data:
        if date_time - data["Date time"] < best_delta:
            best_delta = date_time - data["Date time"]
            best_date_time = data["Date time"]
    return best_date_time

@app.route("/predict", methods=["GET", "POST"])
async def predict_page():
    if request.method == "POST":
        time = get_closest_time(datetime.datetime.fromisoformat(request.form["data-time"]))
        for ele in weather_data:
            if ele["Date time"] == time:
                with open("temp.csv", "w+") as write:
                    writer = csv.writer(write)
                    writer.writerow([list(ele.values())[1:]])
                    return Predictor().predict(write)
        return "Data"
    else:
        return render_template("predictions.html")
