import requests as rq

url = 'https://www.ibm.com/'

r = rq.get(url)

r.status_code = 200 # view request status
r.rq.headers
r.rq.body = json.dumps

print(r)