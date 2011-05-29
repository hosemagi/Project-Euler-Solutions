import math
from datetime import datetime

def isPalindrome(n):
    stringN = str(n)
    reverseN = str(n)[::-1]
    if(stringN == reverseN):
        return True
    return False

def findLargestPalindrome():
    max = -1
    factors = range(100, 1000)
    factors.reverse()
    for i in factors:
        for j in factors:
            product = i*j
            if isPalindrome(product):
                if product > max:
                    print "new max " + str(i) + "*" + str(j) + "=" + str(product)
                    max = product 
    return max

print "Solving..."
starttime = datetime.now()
print "Largest palindrome is " + str(findLargestPalindrome())
endtime = datetime.now()
elapsed = endtime - starttime
print "Solution took " + str(elapsed)