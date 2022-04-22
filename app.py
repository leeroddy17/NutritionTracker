from nntplib import NNTPDataError
from tkinter.messagebox import NO
from flask import Flask, redirect, url_for, render_template, request
from query import *

compare = []

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        searchItem = request.form["foodItem"]
        print(searchItem)
        return redirect(url_for("search", foodItem=searchItem))
    else:
        return render_template("index.html")

@app.route("/about-us")
def about():
    return render_template("about.html")

@app.route("/comparison")
def comparison():
    return render_template("comparison.html",compare = compare)

@app.route("/comparison", methods=["POST"])
def displayOptions():
    if request.method == "POST":
        fields = ['brand_name','item_name','nf_calories']
        try:
            searchItem = request.form["foodItem"]
            print(searchItem)
            hits = querry(searchItem,fields=fields)
            print(hits)
            return render_template("comparison.html",options=hits)
        except:
            try:
                name = request.form.get('add')
                compare.append(querry(name)[0])
            except:
                try:
                    index = request.form.get('remove')
                    compare.pop(int(index))
                except:
                    print('here')
                    return render_template("comparison.html",compare = compare,fields=fields)
            superDict = {}
            for field in fields:
                try:
                    float(compare[0]['fields'][field])
                    superDict[field] = findSuperlatives(compare,field)
                except:
                    superDict[field] = (None,None)
            print(superDict)
            return render_template("comparison.html",compare = compare,fields=fields, superDict = superDict)


@app.route("/<foodItem>")
def search(foodItem):
    rankbyvalue = "nf_calories"

    hits = querry(foodItem)
    increasing = False

    print(hits)
    # print(rankBy(hits, rankbyvalue, increasing))

    return render_template("search.html", item=foodItem, results=hits)


if __name__ == '__main__':
    app.run(debug=True)