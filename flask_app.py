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
        restroom = []
        restroom_url = []
        restroom_image = []
        restroom_review = []
        restroom_rating = []
        restroom_address = []
        restroom_city = []
        restroom_zipcode = []
        restroom_state = []
        for i in range(0, len(v["businesses"])):
            restroom.append(v["businesses"][i]["name"])
            restroom_url.append(v["businesses"][i]["url"])
            restroom_image.append(v["businesses"][i]["image_url"])
            restroom_review.append(v["businesses"][i]["review_count"])
            restroom_rating.append(v["businesses"][i]["rating"])
            restroom_address.append(v["businesses"][i]["location"]["address1"])
            restroom_city.append(v["businesses"][i]["location"]["city"])
            restroom_zipcode.append(v["businesses"][i]["location"]["zip_code"])
            restroom_state.append(v["businesses"][i]["location"]["state"])

        return render_template("index.html", restroom0 = restroom[0], restroom_url0 = restroom_url[0], restroom_image0 = restroom_image[0], restroom_review0 = restroom_review[0], restroom_rating0 = restroom_rating[0], restroom_address0 = restroom_address[0], restroom_city0 = restroom_city[0], restroom_zipcode0 = restroom_zipcode[0], restroom_state0 = restroom_state[0], restroom1 = restroom[1], restroom_url1 = restroom_url[1], restroom_image1 = restroom_image[1], restroom_review1 = restroom_review[1], restroom_rating1 = restroom_rating[1], restroom_address1 = restroom_address[1], restroom_city1 = restroom_city[1], restroom_zipcode1 = restroom_zipcode[1], restroom_state1 = restroom_state[1], restroom2 = restroom[2], restroom_url2 = restroom_url[2], restroom_image2 = restroom_image[2], restroom_review2 = restroom_review[2], restroom_rating2 = restroom_rating[2], restroom_address2 = restroom_address[2], restroom_city2 = restroom_city[2], restroom_zipcode2 = restroom_zipcode[2], restroom_state2 = restroom_state[2], restroom3 = restroom[3], restroom_url3 = restroom_url[3], restroom_image3 = restroom_image[3], restroom_review3 = restroom_review[3], restroom_rating3 = restroom_rating[3], restroom_address3 = restroom_address[3], restroom_city3 = restroom_city[3], restroom_zipcode3 = restroom_zipcode[3], restroom_state3 = restroom_state[3], restroom4 = restroom[4], restroom_url4 = restroom_url[4], restroom_image4 = restroom_image[4], restroom_review4 = restroom_review[4], restroom_rating4 = restroom_rating[4], restroom_address4 = restroom_address[4], restroom_city4 = restroom_city[4], restroom_zipcode4 = restroom_zipcode[4], restroom_state4 = restroom_state[4], restroom5 = restroom[5], restroom_url5 = restroom_url[5], restroom_image5 = restroom_image[5], restroom_review5 = restroom_review[5], restroom_rating5 = restroom_rating[5], restroom_address5 = restroom_address[5], restroom_city5 = restroom_city[5], restroom_zipcode5 = restroom_zipcode[5], restroom_state5 = restroom_state[5], found = found)
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