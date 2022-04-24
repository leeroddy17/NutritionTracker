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

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("/<foodItem>/<servingMult>/")
def search(foodItem, servingMult):
    rankbyvalue = "nf_calories"

    hits = querry(foodItem)
    increasing = False

    print(hits)
    servingMult = int(servingMult)
    # print(rankBy(hits, rankbyvalue, increasing))


    if len(hits) < 10:
        return render_template("error.html", item=foodItem)

    labels = {
        "item_name": "Item name: ",
        "brand_name": "Brand Name: ",
        "nf_calories": "Calories per Serving (cal): ",
        "nf_total_fat": "Total Fat per Serving (g): ",
        "nf_total_carbohydrate": "Total Carbs per Serving (g): ",
        "nf_serving_weight_grams": "Grams in 1 serving (g): ",
        "nf_sodium": "Sodium content per Serving (mg): ",
        "nf_dietary_fiber": "Dietary Fiber per Serving (g): ",
        "nf_sugars": "Total Sugar per Serving (g): ",
        "nf_protein": "Protein per Serving (g): ",
        "nf_vitamin_a_dv": "Vitamin A per Serving (Daily Value %): ",
        "nf_vitamin_c_dv": "Vitamin C per Serving (Daily Value %): ",
        "nf_vitamin_d_mcg": "Vitamin D per Serving (mcg): ",
        "nf_iron_mg": "Iron per Serving (mg): ",
        "nf_calcium_mg": "Calcium per Serving (mg): ",
        "nf_potassium": "Potassium per Serving (mg): ",
        "nf_cholesterol": "Cholesterol per Serving (mg): ",
        "nf_added_sugars": "Added Sugar per Serving (g): ",
        "item_description": "Item Description: ",
        "nf_ingredient_statement": "Ingredient Statement: "
    }

    print(hits[0])

    return render_template("search.html", item=foodItem, mult=servingMult, results=hits, results_length=len(hits), labels=labels)


if __name__ == '__main__':
    app.run(debug=True)