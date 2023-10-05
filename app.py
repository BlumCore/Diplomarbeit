from flask import Flask, render_template
from backend.db import getItem, getLastItems

app = Flask(__name__,  template_folder='templates')


@app.route('/', methods=["GET"])
def index():
    item = getItem()
    lastimes = getLastItems()
    return render_template("index.html", item=item, old=lastimes)

@app.route('/history')
def history():
    item = getItem()
    lastimes = getLastItems()
    return render_template("history.html", item=item, old=lastimes)
