import math
from datetime import datetime

print "Solving..."
starttime = datetime.now()

found = False               # haven't found number yet
num = 20                    # starting state
while not found:            # while we haven't found an answer
    for i in range(2,21):   # begin checking divisibility for each factor in [2,3,...,20] 
        if num % i == 0:    # if the number is divisible by the current factor
            if i == 20:     #     and the current factor is 20
                print num   # we found the answer
                found = True
            else:           # otherwise if the current factor is not 20
                continue    # proceed to check next factor in [2,3,...,20]
        else:               # if the current factor doesn't divide into the number we're testing
            num += 20       # get a new number (must be a multiple of 20 so increase by 20)
            break           # break out of the inner for loop
        
endtime = datetime.now()
elapsed = endtime - starttime
print "Solution took " + str(elapsed)