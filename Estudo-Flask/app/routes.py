from app import app
from flask import render_template, url_for #renderizar arquivo html

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/roupa/")
def secondpage():
    return "Essa é a nova rota"