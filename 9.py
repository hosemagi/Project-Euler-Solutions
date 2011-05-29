#a^2 + b^2 = c^2 and a+b+c=1000
#so c^2 = (a+b-1000)^2 = a^2 + b^2

import math

found = False
for i in range(1, 1000):
    if(found):
        break
    for j in range(1000):
        if (i+j-1000)**2 == i**2 + j**2:
            print (i, j, math.sqrt(i**2 + j**2))
            print int(i*j*math.sqrt(i**2 + j**2))
            found = True
            break
