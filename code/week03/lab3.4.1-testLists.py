# Messing with lists
# Author: andrew Beatty

# demonstrating that a list can have hetrogenious types
aList = [23,'hi', True]

# normal
for item in aList:
    print(item)

# prints out the list in reverse
print ('\n'.join(map(str,aList[::-1])))


# a list of string
# aStringList=['asdf', 'hi', 'asdf']
# print('\n'.join(aStringList))
# 
# but if the list has non string values in it
# then we will need to cast each item to a string

#print ('\n'.join(map(str,aList)))



