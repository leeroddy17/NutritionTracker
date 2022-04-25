from nntplib import NNTPDataError
from tkinter.messagebox import NO
from flask import Flask, redirect, url_for, render_template, request
from query import *
from nutritionx import *

compare = []

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        searchItem = request.form["foodItem"]
        sortCat = request.form["sortCat"]
        sortOrder = request.form["sortOrder"]
        print(searchItem)
        return redirect(url_for("search", foodItem=searchItem, sortCat=sortCat, sortOrder=sortOrder))
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
            sortCat = request.form["sortCat"]
            sortOrder = request.form["sortOrder"]
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

@app.route("/<foodItem>/<sortCat>/<sortOrder>/")
def search(foodItem, sortCat, sortOrder):

    items = get_hits(foodItem)

    if len(items) == 0:
        return render_template("error.html", item=foodItem)

    hits = []
    for item in items:
        hits.append(get_facts(item))

    if sortOrder == "ascending":
        sortOrder = True
    else:
        sortOrder = False

    hits = rankBy(hits, sortCat, sortOrder)

    class_labels = []
    for i in range(0, 10):
        class_labels.append("list-" + str(i))

    id_labels = []
    for i in range(0, 10):
        id_labels.append("list-" + str(i) + "-list")

    href_labels = []
    for i in range(0, 10):
        href_labels.append("#" + "list-" + str(i))


    labels = {
        "food_name": "Item name: ",
        "serving_unit": "Serving Unit: ",
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

    print(class_labels)
    print(href_labels)
    print(id_labels)
    return render_template("top_result.html", item=foodItem, results=hits, results_length=len(hits), labels=labels,
                           class_labels=class_labels, href_labels=href_labels, id_labels=id_labels)

# @app.route("/<foodItem>/")
# def search(foodItem):
#     rankbyvalue = "nf_calories"
#
#     hits = querry(foodItem)
#     increasing = False
#
#
#     class_labels = []
#     for i in range(0, 10):
#         class_labels.append("list-" + str(i))
#
#     id_labels = []
#     for i in range(0, 10):
#         id_labels.append("list-" + str(i) + "-list")
#
#     href_labels = []
#     for i in range(0, 10):
#         href_labels.append("#" + "list-" + str(i))
#
#
#     if len(hits) < 10:
#         return render_template("error.html", item=foodItem)
#
#     labels = {
#         "item_name": "Item name: ",
#         "brand_name": "Brand Name: ",
#         "nf_calories": "Calories per Serving (cal): ",
#         "nf_total_fat": "Total Fat per Serving (g): ",
#         "nf_total_carbohydrate": "Total Carbs per Serving (g): ",
#         "nf_serving_weight_grams": "Grams in 1 serving (g): ",
#         "nf_sodium": "Sodium content per Serving (mg): ",
#         "nf_dietary_fiber": "Dietary Fiber per Serving (g): ",
#         "nf_sugars": "Total Sugar per Serving (g): ",
#         "nf_protein": "Protein per Serving (g): ",
#         "nf_vitamin_a_dv": "Vitamin A per Serving (Daily Value %): ",
#         "nf_vitamin_c_dv": "Vitamin C per Serving (Daily Value %): ",
#         "nf_vitamin_d_mcg": "Vitamin D per Serving (mcg): ",
#         "nf_iron_mg": "Iron per Serving (mg): ",
#         "nf_calcium_mg": "Calcium per Serving (mg): ",
#         "nf_potassium": "Potassium per Serving (mg): ",
#         "nf_cholesterol": "Cholesterol per Serving (mg): ",
#         "nf_added_sugars": "Added Sugar per Serving (g): ",
#         "item_description": "Item Description: ",
#         "nf_ingredient_statement": "Ingredient Statement: "
#     }
#
#     return render_template("top_result.html", item=foodItem, results=hits, results_length=len(hits), labels=labels,
#                            class_labels=class_labels, href_labels=href_labels, id_labels=id_labels)


if __name__ == '__main__':
    app.run(debug=True)