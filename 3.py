import math
from datetime import datetime

# returns the largest prime factor of a number n
def largestPrimeFactor(n):
    # check for base case
    if n == 2:
        return 2
    
    # initialize first prime to 3
    i = 3
    
    # loop until we find the largest prime
    while True:
        # if n is divisible by the current number
        if(n % i == 0):
            # get the corresponding factor (this is an optimization)
            # e.g. if n=20 and we're checking 4, then the siblingFactor is 5
            # this allows us to check the greatest factors in the list first
            siblingFactor = n/i
            
            # if the siblingFactor is prime we know it must be the largest
            # since we're processing the factors in order from greatest to least
            # therefore, the first prime siblingFactor we find must be the largest prime factor
            if numberIsPrime(siblingFactor):
                return siblingFactor
        # otherwise add 2 to the number to avoid checking even numbers
        i += 2

# returns True if a number n is prime, False otherwise
def numberIsPrime(n):
    # check for base cases
    if n < 2:
        return False
    if n == 2:
        return True
    
    # check for divisibility among list of primes
    for i in range(2, int(math.floor(math.sqrt(n)))+1):
        # if n is evenly divisible by a prime then it cannot be prime itself
        if n % i == 0:
            return False
    # otherwise n is prime
    return True

print "Solving..."
starttime = datetime.now()
print "Largest prime factor of 600851475143 is " + str(largestPrimeFactor(600851475143))
endtime = datetime.now()
elapsed = endtime - starttime
print "Solution took " + str(elapsed)

        
        