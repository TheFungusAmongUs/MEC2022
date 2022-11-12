from flask import Flask

app = Flask(__name__)


@app.route("/")
async def home():
    return ""

# a change
@app.route("/logs")
async def logs_page():
    return "Here are the logs:"


@app.route("/test")
async def test_page():
    return "Toggle test mode:"


@app.route("/settings")
async def settings_page():
    return "settings"
