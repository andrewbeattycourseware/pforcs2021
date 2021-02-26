# program that gets al the ip addresses from a file
# Author: Andrew Beatty

import re

filename="sample.log"
path="../logs/www2/"

with open (path+filename, "r") as logFile:
    count= 0
    for line in logFile:
       
        regex = "^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
        ip = re.findall(regex, line)
        print(ip[0])
        count +=1

print("fin ", count)
