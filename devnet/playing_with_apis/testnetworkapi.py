import requests
url = "https://123.123.123.123/dna/intent/api/v1/network-device"
resp = requests.get(url, verify = False)
print(resp)
