import math
number = 600851475143

def isPrime(number):
    for x in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % x == 0:
            return False
    if number <= 1:
        return False
    else:
        return True

# Find factors
factors = []
for factor in range(math.ceil(math.sqrt(number)))[1::]:
    if number % factor == 0:
        factors.append(factor)

# print(factors)

for factor in factors[::-1]:
    if isPrime(factor):
        print(factor)
        exit()