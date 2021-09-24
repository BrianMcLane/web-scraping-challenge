from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsdb"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    webitems = mongo.db.webitems.find_one()
    print(webitems)
    return render_template("index.html", webitems=webitems)


@app.route("/scrape")
def scraper():
    webitems = mongo.db.webitems
    listings_data = scrape_mars.scrape()
    webitems.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
