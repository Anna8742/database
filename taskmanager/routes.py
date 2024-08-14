from flask import render_template
from taskmanager import app, db


@app.router('/')
def home():
    return render_template("base.html")