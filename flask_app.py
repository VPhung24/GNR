import sys
from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask import *
from functools import wraps
import yelp_f
import config
from http import *

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

@app.route("/", methods=["GET","POST"])
def main_route():
    if request.method == "POST":
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
        restroom_true = []
        error = " "
        g = len(v["businesses"])
        v = v["businesses"]
        if (not len(location_user) == 5):
            found = False
            error = "Sorry! Please input a zipcode."
            return render_template("index.html", error = error, found = found)
        elif (len(type_user) <= 3):
            found = False
            error = "Sorry! Please input more characters for Type of Establishment."
            return render_template("index.html", error = error, found = found)
        elif (g == 0) or (not g):
            found = False
            error = "Sorry! We don't know of any Gender Neutral Restrooms in your area of the type you specified. Please try again!"
            return render_template("index.html", error = error, found = found)
        elif g == 6:
            found = True
            three_or_less = False
            for i in range(0, g):
                restroom.append(v[i]["name"])
                restroom_url.append(v[i]["url"])
                restroom_image.append(v[i]["image_url"]) 
                restroom_review.append(v[i]["review_count"])
                restroom_rating.append(v[i]["rating"])
                restroom_address.append(v[i]["location"]["address1"])
                restroom_city.append(v[i]["location"]["city"])
                restroom_zipcode.append(v[i]["location"]["zip_code"])
                restroom_state.append(v[i]["location"]["state"])
                restroom_true.append(True)
            return render_template("index.html", three_or_less = three_or_less,  restroom_true1 = restroom_true[1], restroom_true2 = restroom_true[2], restroom_true3 = restroom_true[3], restroom_true4 = restroom_true[4], restroom_true5 = restroom_true[5], restroom0 = restroom[0], restroom_url0 = restroom_url[0], restroom_image0 = restroom_image[0], restroom_review0 = restroom_review[0], restroom_rating0 = restroom_rating[0], restroom_address0 = restroom_address[0], restroom_city0 = restroom_city[0], restroom_zipcode0 = restroom_zipcode[0], restroom_state0 = restroom_state[0], restroom1 = restroom[1], restroom_url1 = restroom_url[1], restroom_image1 = restroom_image[1], restroom_review1 = restroom_review[1], restroom_rating1 = restroom_rating[1], restroom_address1 = restroom_address[1], restroom_city1 = restroom_city[1], restroom_zipcode1 = restroom_zipcode[1], restroom_state1 = restroom_state[1], restroom2 = restroom[2], restroom_url2 = restroom_url[2], restroom_image2 = restroom_image[2], restroom_review2 = restroom_review[2], restroom_rating2 = restroom_rating[2], restroom_address2 = restroom_address[2], restroom_city2 = restroom_city[2], restroom_zipcode2 = restroom_zipcode[2], restroom_state2 = restroom_state[2], restroom3 = restroom[3], restroom_url3 = restroom_url[3], restroom_image3 = restroom_image[3], restroom_review3 = restroom_review[3], restroom_rating3 = restroom_rating[3], restroom_address3 = restroom_address[3], restroom_city3 = restroom_city[3], restroom_zipcode3 = restroom_zipcode[3], restroom_state3 = restroom_state[3], restroom4 = restroom[4], restroom_url4 = restroom_url[4], restroom_image4 = restroom_image[4], restroom_review4 = restroom_review[4], restroom_rating4 = restroom_rating[4], restroom_address4 = restroom_address[4], restroom_city4 = restroom_city[4], restroom_zipcode4 = restroom_zipcode[4], restroom_state4 = restroom_state[4], restroom5 = restroom[5], restroom_url5 = restroom_url[5], restroom_image5 = restroom_image[5], restroom_review5 = restroom_review[5], restroom_rating5 = restroom_rating[5], restroom_address5 = restroom_address[5], restroom_city5 = restroom_city[5], restroom_zipcode5 = restroom_zipcode[5], restroom_state5 = restroom_state[5], found = found)
        elif g < 6:
            found = True
            z = 6 - g
            for i in range(0, g):
                restroom.append(v[i]["name"])
                restroom_url.append(v[i]["url"])
                restroom_image.append(v[i]["image_url"])
                restroom_review.append(v[i]["review_count"])
                restroom_rating.append(v[i]["rating"])
                restroom_address.append(v[i]["location"]["address1"])
                restroom_city.append(v[i]["location"]["city"])
                restroom_zipcode.append(v[i]["location"]["zip_code"])
                restroom_state.append(v[i]["location"]["state"])
                restroom_true.append(True)
            for v in range(0, z):
                restroom.append("name")
                restroom_url.append("url")
                restroom_image.append("image_url")
                restroom_review.append("review_count")
                restroom_rating.append("rating")
                restroom_address.append("address1")
                restroom_city.append("city")
                restroom_zipcode.append("zip_code")
                restroom_state.append("state")
                restroom_true.append(False)
            if z >= 3:
                three_or_less = True
            else:
                three_or_less = False
            return render_template("index.html", three_or_less = three_or_less, restroom_true1 = restroom_true[1], restroom_true2 = restroom_true[2], restroom_true3 = restroom_true[3], restroom_true4 = restroom_true[4], restroom_true5 = restroom_true[5], restroom0 = restroom[0], restroom_url0 = restroom_url[0], restroom_image0 = restroom_image[0], restroom_review0 = restroom_review[0], restroom_rating0 = restroom_rating[0], restroom_address0 = restroom_address[0], restroom_city0 = restroom_city[0], restroom_zipcode0 = restroom_zipcode[0], restroom_state0 = restroom_state[0], restroom1 = restroom[1], restroom_url1 = restroom_url[1], restroom_image1 = restroom_image[1], restroom_review1 = restroom_review[1], restroom_rating1 = restroom_rating[1], restroom_address1 = restroom_address[1], restroom_city1 = restroom_city[1], restroom_zipcode1 = restroom_zipcode[1], restroom_state1 = restroom_state[1], restroom2 = restroom[2], restroom_url2 = restroom_url[2], restroom_image2 = restroom_image[2], restroom_review2 = restroom_review[2], restroom_rating2 = restroom_rating[2], restroom_address2 = restroom_address[2], restroom_city2 = restroom_city[2], restroom_zipcode2 = restroom_zipcode[2], restroom_state2 = restroom_state[2], restroom3 = restroom[3], restroom_url3 = restroom_url[3], restroom_image3 = restroom_image[3], restroom_review3 = restroom_review[3], restroom_rating3 = restroom_rating[3], restroom_address3 = restroom_address[3], restroom_city3 = restroom_city[3], restroom_zipcode3 = restroom_zipcode[3], restroom_state3 = restroom_state[3], restroom4 = restroom[4], restroom_url4 = restroom_url[4], restroom_image4 = restroom_image[4], restroom_review4 = restroom_review[4], restroom_rating4 = restroom_rating[4], restroom_address4 = restroom_address[4], restroom_city4 = restroom_city[4], restroom_zipcode4 = restroom_zipcode[4], restroom_state4 = restroom_state[4], restroom5 = restroom[5], restroom_url5 = restroom_url[5], restroom_image5 = restroom_image[5], restroom_review5 = restroom_review[5], restroom_rating5 = restroom_rating[5], restroom_address5 = restroom_address[5], restroom_city5 = restroom_city[5], restroom_zipcode5 = restroom_zipcode[5], restroom_state5 = restroom_state[5], found = found)
        else:
            found = False
            error = "Sorry! There's another error please email vivianphung@outlook.com"
            return render_template("index.html", found = found, error = error)
    else:
        found = False
        return render_template("index.html", found = found)

app.secret_key = 'GNR for life'

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
if __name__ == '__main__':
    # listen on external IPs
    http.ListenAndServe("107.170.18.23:8080", nil)
