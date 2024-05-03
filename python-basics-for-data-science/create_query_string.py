import requests

url = 'http://httpbin.org/get'
payload = {"name": "Joseph", "ID":"123"}

r = requests.get(url)
r.url:'http://httpbin.org/get?name=Joseph&ID=123'
print(r.status_code)