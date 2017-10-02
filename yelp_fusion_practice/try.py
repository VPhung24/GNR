from __future__ import print_function
import argparse
import json
import pprint
import requests
import sys
import urllib

try:
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

CLIENT_ID = "zBGkYQVe0aicViSmzj9SPg"
CLIENT_SECRET = "bADttn0PFCMqiqgICFLOTz1WzUMyGXsBwnzjE0gd4vm1nUrpyMovpDCBR9bWja3z"

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 6


def obtain_bearer_token(host, path):
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "zBGkYQVe0aicViSmzj9SPg"
    assert CLIENT_SECRET, "bADttn0PFCMqiqgICFLOTz1WzUMyGXsBwnzjE0gd4vm1nUrpyMovpDCBR9bWja3z"
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token


def request(host, path, bearer_token, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(bearer_token, term, location):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'attributes': "gender_neutral_restrooms"

    }
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)

def get_business(bearer_token, business_id):
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path, bearer_token)

def query_api(term, location):

    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)

    response = search(bearer_token, term, location)
    
    return response
v = query_api("sushi", "94501")
print(v)
g = len(v["businesses"])
print(g)
restroom = []
restroom_url = []
restroom_image = []
restroom_review = []
restroom_rating = []
restroom_address = []
restroom_city = []
restroom_zipcode = []
restroom_state = []
for i in range(0, g - 1):
    restroom.append(i) = v["businesses"][i]["name"]
    restroom_url.append(i) = v["businesses"][i]["url"]
    restroom_image.append(i) = v["businesses"][i]["image_url"]
    restroom_review.append(i) = v["businesses"][i]["review_count"]
    restroom_rating.append(i) = v["businesses"][i]["rating"]
    restroom_address.append(i) = v["businesses"][i]["location"]["address1"]
    restroom_city.append(i) = v["businesses"][i]["location"]["city"]
    restroom_zipcode.append(i) = v["businesses"][i]["location"]["zip_code"]
    restroom_state.append(i) = v["businesses"][i]["location"]["state"]
    print(restroom)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')
    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )
main()
