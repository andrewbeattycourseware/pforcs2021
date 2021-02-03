# program to split a string

inputString = input("please enter a string")

outputList = inputString.split(',')

for output in outputList:
    print (output)

lastFive = inputString[-5::-1]
print(lastFive)