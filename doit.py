from flask import Flask
app = Flask(__name__)

@app.route("/funnels")
def funnels():
    return "Hello OK!"



@app.route("/funnels/summary")
def funnels_summary():
    return "Hello OK2!"
