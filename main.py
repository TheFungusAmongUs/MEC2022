from flask import Flask

app = Flask(__name__)


@app.route("/")
async def home():
    return ""


@app.route("/logs")
async def logs_page():
    return "Here are the logs:"


@app.route("/test")
async def test_page():
    return "Toggle test mode:"
