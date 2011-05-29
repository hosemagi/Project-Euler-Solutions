import math
from datetime import datetime

print "Solving..."
starttime = datetime.now()                      # record start time for time profiling

# define a function that takes a number and returns the sum of its digits
def sumOfDigits(number):
    # convert the number to a string representation
    stringRepresentation = str(number)
    
    # start the running sum at 0
    sumOfDigits = 0
    
    # for each character at index 'i' in the string representation of the number
    for i in range(len(stringRepresentation)):
        # convert the digit into an integer
        digit = int(stringRepresentation[i])
        
        #add the integer to the running sum
        sumOfDigits += digit
        
    # return the calculated sum of the digits
    return sumOfDigits

# get the value of 100!
oneHundredFactorial = math.factorial(100)

# pass the integer value of 100! to the sumOfDigits function and print its return value
print sumOfDigits(oneHundredFactorial)


endtime = datetime.now()                        # record end time for time profiling
elapsed = endtime - starttime                   # calculate running time
print "Solution took " + str(elapsed)           # print running time