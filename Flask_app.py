from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import flask
import scrape_mars

# Create an instance of Flask website
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_mars_db"
mongodb_client = PyMongo(app)
results_collection = mongodb_client.db.Result_Dicts

# Route to render index.html (Home page) template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    Result_Dict = results_collection.find_one()
    # Return template and data
    return render_template("index.html", mars=Result_Dict)

# route to Scrape method - accessed from the button on the home page.
@app.route("/scrape")
def scrape_and_update_db():
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    results_collection.update({}, mars_data, upsert = True)
    return redirect("/")

#If the wesite is live, then debug=false but since website (development) is not live, debug is True.
if __name__ == "__main__":
    app.run(debug=True)