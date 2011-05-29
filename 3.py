import math
from datetime import datetime

def largestPrime(n):
    for i in xrange(2, n):
        if(n % i == 0):
            siblingFactor = n/i
            if numberIsPrime(siblingFactor):
                return siblingFactor

def numberIsPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.floor(math.sqrt(n)))+1):
        if n % i == 0:
            #print str(n) + " divisible by " + str(i)
            return False
    return True

print "Solving..."
starttime = datetime.now()
print "Largest prime factor of 600851475143 is " + str(largestPrime(600851475143))
endtime = datetime.now()
elapsed = endtime - starttime
print "Solution took " + str(elapsed)

        
        