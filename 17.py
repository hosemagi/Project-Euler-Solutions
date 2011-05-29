import math
from datetime import datetime

print "Solving..."
starttime = datetime.now()                      # record start time for time profiling



endtime = datetime.now()                        # record end time for time profiling
elapsed = endtime - starttime                   # calculate running time
print "Solution took " + str(elapsed)           # print running time