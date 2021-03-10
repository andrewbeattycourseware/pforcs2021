# test search

import re

string= "hello mom. how are you. love me."

regex="\.[\w ]+."


found = re.search(regex, string)

print(found.group())

regex = "^[\w ]+\. "
smaller = re.sub(regex,'', string)
regex = "\.[\w ]+\.$"
found = re.sub(regex, '', smaller)
print (found)