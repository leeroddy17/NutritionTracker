from flask import Flask, redirect, url_for, render_template, request
from query import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        searchItem = request.form["foodItem"]
        searchMult = request.form["servingMult"]
        print(searchItem)
        return redirect(url_for("search", foodItem=searchItem, servingMult=searchMult))
    else:
        return render_template("index.html")

@app.route("/about-us")
def about():
    return render_template("about.html")

@app.route("/<foodItem>/<servingMult>/")
def search(foodItem, servingMult):
    rankbyvalue = "nf_calories"

    hits = querry(foodItem)
    increasing = False

    print(hits)
    # print(rankBy(hits, rankbyvalue, increasing))

    return render_template("search.html", item=foodItem, mult=servingMult, results=hits)


if __name__ == '__main__':
    app.run(debug=True)