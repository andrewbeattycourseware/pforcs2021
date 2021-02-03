# messing with lists
# author: Andrew Beatty


aList = [23, 'joe', True, [1,2,3], 33]

for item in aList:
    print ('list item {}, has type {}'.format(item, type(item)))

print (aList[3][0])

queue = []

queue.append(4)
queue.append("hi")
queue.append(5)
queue.append(6)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

listOfNumbers1 = []
for item in aList:
    if type(item) == int:
        listOfNumbers1.append(item)
print(listOfNumbers1)

listOfNumbers2 = [x**2 for x in aList if type(x) == int]
print(listOfNumbers2)
