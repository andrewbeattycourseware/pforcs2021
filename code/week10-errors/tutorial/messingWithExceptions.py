# messing with exceptions
# how to handle two at the same time
# a quick search will lead me to
# what you can do
# https://pythonbasics.org/try-except/

# What you can do
# https://stackoverflow.com/questions/12826291/raise-two-errors-at-the-same-time


try:
    #pass
    #divisor = 10
    divisor = 0
    index = 100
    aList = [1, 2]
    a = aList[index] // divisor

    print ("no errors")

# here we catch the two errors at the same time
except (ZeroDivisionError, IndexError) as e :
    print('error:', e)
# or you can catch another error seperatly
except IndexError:
    print ("index out of bounds")



print ("the end")