#!/usr/bin/python3
import requests

obtener = requests.get('https://icanhazdadjoke.com')
print("========================")
print(obtener.status_code)
print("========================")
print(obtener)