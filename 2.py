previous = 1
current = 1
sum = 0
while(current < 4000000):
    if current % 2 == 0:
        sum += current
    oldprevious = previous
    previous = current
    current = oldprevious + current  
print sum 
    
