import requests

url = "https://api.meraki.com/api/v0/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '8f90ecec4fca692f606092279f203c6020ca011c',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


