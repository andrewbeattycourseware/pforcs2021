# demo split
import re


string = "joe\tfred,mike, mary: greg "

regex = "\W+"

listOfNames = re.split(regex, string.strip())
print (listOfNames)