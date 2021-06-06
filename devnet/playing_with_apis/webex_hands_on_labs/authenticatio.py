# Fill in this file with the authentication code from the Webex Teams exercise

import requests
import json
# This access token may be a (limited duration) personal access token, a Bot token, or an OAuth token from an Integration or Guest Issuer application.
# IMPORTANT
# Make sure to replace access_token with YOUR access token.
access_token = 'Q2F4OWUzZDQtNjdjZC00N2E0LWE3NGUtM2Q5ZTU4ZDQ2OTU5ODczYjZiNzEtYmE0_PF84_1eb65fdf-9743-417f-9974-af72cae0e10f'
url = 'https://api.ciscospark.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

