# sample http request
# author: Andrew Beatty

import requests

host = 'http://andrewbeatty1.pythonanywhere.com'
url = host + '/books'

response = requests.get(url)
print(response.status_code)
print(response.content)
