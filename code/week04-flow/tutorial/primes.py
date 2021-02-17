# script for generating primes
# Author Andrew Beatty
import math

primes = []
upto = 1000

def isPrime(cadidate):
    # check if it is a prime
    for divisor in range(2, math.floor(math.sqrt(cadidate))):
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
