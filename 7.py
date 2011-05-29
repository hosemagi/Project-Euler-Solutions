import math

primes = [2,3,5,7,11,13]
num = 14
while len(primes) < 10001:
    isPrime = True
    for i in range(len(primes)):
        if(i > math.sqrt(num)):
            break
        if num % primes[i] == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(num)
        print "Prime " + str(len(primes)) + ": " + str(num)
    num += 1
    

        

