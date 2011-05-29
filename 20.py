import math
from datetime import datetime

print "Solving..."
starttime = datetime.now()

def sumOfDigits(number):
    stringRepresentation = str(number)
    sumOfDigits = 0
    for i in range(len(stringRepresentation)):
        digit = int(stringRepresentation[i])
        sumOfDigits += digit
    return sumOfDigits

oneHundredFactorial = math.factorial(100)
print sumOfDigits(oneHundredFactorial)


endtime = datetime.now()
elapsed = endtime - starttime
print "Solution took " + str(elapsed)