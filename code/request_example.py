import requests

r = requests.get("https://api.github.com/events",timeout=5)

r.status_code

r.headers['content-type']

r.encoding

r.text