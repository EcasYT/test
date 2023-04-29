import requests

s = requests.get("http://google.com")
print(s.json)