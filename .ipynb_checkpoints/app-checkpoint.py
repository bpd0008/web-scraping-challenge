
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)


@app.route("/")
def home():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars_df=mars)


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    
    mars_df = scrape_mars.scrape()
    
    mars.update(
        {}, 
        mars_df, 
        upsert=True
    )

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)