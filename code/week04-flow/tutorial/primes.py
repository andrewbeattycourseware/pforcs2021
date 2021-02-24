# script for generating primes
# Author Andrew Beatty
import math

primes = []
upto = 1000


def isPrime(candidate):
    # check if it is a prime
    # error fixed the floor of the sqrt of 8 is 2 and range goes to one less than that
    # so I have added one to it (I do this instead of ceiling to deal with 4)
    for divisor in range(2, math.floor(math.sqrt(candidate))+1):
        if candidate % divisor == 0:
            return False
    return True


candidates = range(2,upto+1)
#print (type(candidates))
for candidate in candidates:
    # if it is still a prime
    if isPrime(candidate):
        primes.append(candidate)

print (primes)
