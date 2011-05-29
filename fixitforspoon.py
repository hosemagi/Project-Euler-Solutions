import math

def primefactor(n):

    listofprimes = []

    for x in range(2, int(math.ceil(math.sqrt(n) + 1))):
        if n % x == 0:
            return False
    return True

for z in range(2, 1000):
    isprime = primefactor(z)
    if isprime != 1:
        listofprimes.append(z)

print(listofprimes)