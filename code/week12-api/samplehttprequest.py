# sample http request
# author: Andrew Beatty

import requests



host = 'http://127.0.0.1:5000'
url = host + '/cars'
data = {'reg':'123','make':'blah','model':'blah','price':1234}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
