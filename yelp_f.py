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

def postalValidate(S):
   S = S.replace(" ","") 
   if len(S) != 6 or S.isalpha() or S.isdigit(): 
      return False  
   if not S[0:5:2].isalpha(): 
      return False  
   if not S[1:6:2].isdigit(): 
      return False 
   return S.upper()  

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
