import math
from datetime import datetime

print "Solving..."
starttime = datetime.now()                      # record start time for time profiling

sum = sum([i**i for i in range(1, 1001)])
stringRepresentation = str(sum)
endIndex = len(stringRepresentation)
startIndex = endIndex - 10
lastTenDigits = stringRepresentation[startIndex:endIndex]
print lastTenDigits

endtime = datetime.now()                        # record end time for time profiling
elapsed = endtime - starttime                   # calculate running time
print "Solution took " + str(elapsed)           # print running time