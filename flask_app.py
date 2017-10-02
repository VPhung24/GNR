from flask import Flask
import sys
from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask import *
from functools import wraps
import yelp_f

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

@app.route("/", methods=["GET","POST"])
def main_route():
    if request.method == "POST":
        found = True
        location_user = request.form['location']
        type_user = request.form['type']
        v = yelp_f.query_api(type_user, location_user)

        # restroom1
        restroom1 = v["businesses"][0]["name"]
        restroom1_url = v["businesses"][0]["url"]
        restroom1_image = v["businesses"][0]["image_url"]
        restroom1_review = v["businesses"][0]["review_count"]
        restroom1_rating = v["businesses"][0]["rating"]
        restroom1_address = v["businesses"][0]["location"]["address1"]
        restroom1_city = v["businesses"][0]["location"]["city"]
        restroom1_zipcode = v["businesses"][0]["location"]["zip_code"]
        restroom1_state = v["businesses"][0]["location"]["state"]

        # restroom2
        restroom2 = v["businesses"][1]["name"]
        restroom2_url = v["businesses"][1]["url"]
        restroom2_image = v["businesses"][1]["image_url"]
        restroom2_review = v["businesses"][1]["review_count"]
        restroom2_rating = v["businesses"][1]["rating"]
        restroom2_address = v["businesses"][1]["location"]["address1"]
        restroom2_city = v["businesses"][1]["location"]["city"]
        restroom2_zipcode = v["businesses"][1]["location"]["zip_code"]
        restroom2_state = v["businesses"][1]["location"]["state"]

        # restroom3
        restroom3 = v["businesses"][2]["name"]
        restroom3_url = v["businesses"][2]["url"]
        restroom3_image = v["businesses"][2]["image_url"]
        restroom3_review = v["businesses"][2]["review_count"]
        restroom3_rating = v["businesses"][2]["rating"]
        restroom3_address = v["businesses"][2]["location"]["address1"]
        restroom3_city = v["businesses"][2]["location"]["city"]
        restroom3_zipcode = v["businesses"][2]["location"]["zip_code"]
        restroom3_state = v["businesses"][2]["location"]["state"]

        # restroom4
        restroom4 = v["businesses"][3]["name"]
        restroom4_url = v["businesses"][3]["url"]
        restroom4_image = v["businesses"][3]["image_url"]
        restroom4_review = v["businesses"][3]["review_count"]
        restroom4_rating = v["businesses"][3]["rating"]
        restroom4_address = v["businesses"][3]["location"]["address1"]
        restroom4_city = v["businesses"][3]["location"]["city"]
        restroom4_zipcode = v["businesses"][3]["location"]["zip_code"]
        restroom4_state = v["businesses"][3]["location"]["state"]

        # restroom5
        restroom5 = v["businesses"][4]["name"]
        restroom5_url = v["businesses"][4]["url"]
        restroom5_image = v["businesses"][4]["image_url"]
        restroom5_review = v["businesses"][4]["review_count"]
        restroom5_rating = v["businesses"][4]["rating"]
        restroom5_address = v["businesses"][4]["location"]["address1"]
        restroom5_city = v["businesses"][4]["location"]["city"]
        restroom5_zipcode = v["businesses"][4]["location"]["zip_code"]
        restroom5_state = v["businesses"][4]["location"]["state"]

        # restroom6
        restroom6 = v["businesses"][5]["name"]
        restroom6_url = v["businesses"][5]["url"]
        restroom6_image = v["businesses"][5]["image_url"]
        restroom6_review = v["businesses"][5]["review_count"]
        restroom6_rating = v["businesses"][5]["rating"]
        restroom6_address = v["businesses"][5]["location"]["address1"]
        restroom6_city = v["businesses"][5]["location"]["city"]
        restroom6_zipcode = v["businesses"][5]["location"]["zip_code"]
        restroom6_state = v["businesses"][5]["location"]["state"]

        return render_template("index.html", restroom1 = restroom1, restroom1_url = restroom1_url, restroom1_image = restroom1_image, restroom1_review = restroom1_review, restroom1_rating = restroom1_rating, restroom1_address = restroom1_address, restroom1_city = restroom1_city, restroom1_zipcode = restroom1_zipcode, restroom1_state = restroom1_state, restroom2 = restroom2, restroom2_url = restroom2_url, restroom2_image = restroom2_image, restroom2_review = restroom2_review, restroom2_rating = restroom2_rating, restroom2_address = restroom2_address, restroom2_city = restroom2_city, restroom2_zipcode = restroom2_zipcode, restroom2_state = restroom2_state, restroom3 = restroom3, restroom3_url = restroom3_url, restroom3_image = restroom3_image, restroom3_review = restroom3_review, restroom3_rating = restroom3_rating, restroom3_address = restroom3_address, restroom3_city = restroom3_city, restroom3_zipcode = restroom3_zipcode, restroom3_state = restroom3_state, restroom4 = restroom4, restroom4_url = restroom4_url, restroom4_image = restroom4_image, restroom4_review = restroom4_review, restroom4_rating = restroom4_rating, restroom4_address = restroom4_address, restroom4_city = restroom4_city, restroom4_zipcode = restroom4_zipcode, restroom4_state = restroom4_state, restroom5 = restroom5, restroom5_url = restroom5_url, restroom5_image = restroom5_image, restroom5_review = restroom5_review, restroom5_rating = restroom5_rating, restroom5_address = restroom5_address, restroom5_city = restroom5_city, restroom5_zipcode = restroom5_zipcode, restroom5_state = restroom5_state, restroom6 = restroom6, restroom6_url = restroom6_url, restroom6_image = restroom6_image, restroom6_review = restroom6_review, restroom6_rating = restroom6_rating, restroom6_address = restroom6_address, restroom6_city = restroom6_city, restroom6_zipcode = restroom6_zipcode, restroom6_state = restroom6_state, found = found)
    found = False
    return render_template("index.html", found = found)

app.secret_key = 'vivian and serina is cool'

@app.errorhandler(404)
def page_not_found(e):
	options = {
	    "edit": False
	}
	return render_template("404.html" , **options)

@app.errorhandler(405)
def method_not_found(e):
	options = {
		"edit": False
	}
	return render_template("405.html" , **options)

@app.route('/slashboard/')
def slashboard():
	try:
		return render_template("index.html")
	except Exception as e:
		return render_template("500.html", error = e)