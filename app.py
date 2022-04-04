from flask import Flask, redirect, url_for, render_template
from query import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    queryterm = "cheddar cheese"
    rankbyvalue = "nf_calories"

    hits = querry(queryterm)
    increasing = False

    print(rankBy(hits, rankbyvalue, increasing))


@app.route("/test")
def test():
    return render_template("newpage.html")


if __name__ == '__main__':
    app.run(debug=True)