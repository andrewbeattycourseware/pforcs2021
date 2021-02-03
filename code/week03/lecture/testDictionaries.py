# messing with dictionaries
# Author: Andrew Beatty

aDict ={
    "amount": 34,
    "name" : "Andrew"
    }

#print (type(aDict))
#print ("aDict is:" + str(aDict))
#print (aDict["name33"])
print (aDict.get("name33"))

aDict["age"] = 33
aDict.update({"name":"Fred", "account":"checking"})

print(aDict)
"""
for key in aDict:
    print(key + ":" + str(aDict[key]))
"""
#print (aDict.items())
for key , value in aDict.items():
    print (key + "\t:" + str(value))