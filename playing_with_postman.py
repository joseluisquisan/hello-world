import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
