import math

sumOfSquares = sum([i**2 for i in range(1, 101)])
squareOfSum = sum([i for i in range(1, 101)])**2
print abs(squareOfSum - sumOfSquares)