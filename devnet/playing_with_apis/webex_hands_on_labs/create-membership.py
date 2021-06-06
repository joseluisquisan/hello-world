# Fill in this file with the membership code from the Webex Teams exercise

import requests

access_token = ''  # Make sure to add your access token here
room_id = ''
url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())

import requests

access_token = ''  # Make sure to add your access token here
room_id = '' # Add the room Id from the previous example
person_email = '' # Add the email address of someone with a Webex Teams account
url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())

