import requests

url_post = "http://httpbin.org/post"
payload = {"name": "Joseph", "ID":"123"}
r_post = requests.post(url_post,data=payload)