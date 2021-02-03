# messing around with HTTP requests
# Author: Andrew Beatty

import requests

# url = "https://www.gmit.ie/"
#url = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)

bitCoinDict = returnedData.json()

print(bitCoinDict)
