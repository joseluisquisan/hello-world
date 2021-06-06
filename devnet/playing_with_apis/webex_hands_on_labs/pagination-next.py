# Fill in this file with the authentication code from the Webex Teams exercise

import requests
import json
# This access token may be a (limited duration) personal access token, a Bot token, or an OAuth token from an Integration or Guest Issuer application.
# IMPORTANT
# Make sure to replace access_token with YOUR access token.
access_token = ''
url = 'https://api.ciscospark.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

import requests
import json

access_token = '' # Make sure to add your access token here!
url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    "max": 1
}
res = requests.get(url, headers=headers, params=params)
formatted_message = """
Webex Teams API Response
----------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-----------------------------------
""".format(res.status_code,  res.headers.get('Link'), json.dumps(res.json(), indent=4))
print(formatted_message)

# Make the next paginated API request
import requests
import json

access_token = ''  # Make sure to add your access token here
url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    "max": 1
}
res = requests.get(url, headers=headers, params=params)

second_response = requests.get(res.links['next']['url'], headers=headers)
formatted_message = """
Webex Teams Second API Response
----------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-----------------------------------
""".format(second_response.status_code,  second_response.headers.get('Link'), json.dumps(second_response.json(), indent=4))
print(formatted_message)

