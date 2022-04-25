from flask import Flask, redirect, url_for, render_template, request
from query import *
from nutritionx import *

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
    return render_template("comparison.html")

@app.route("/<foodItem>/")
def search(foodItem):

    items = get_hits(foodItem)

    if len(items) == 0:
        return render_template("error.html", item=foodItem)

    hits = []
    for item in items:
        hits.append(get_facts(item))


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