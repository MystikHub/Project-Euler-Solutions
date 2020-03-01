# Largest palindrome that's a product of two 3-digit numbers
# - Factors are between 100 and 999
# - Possible palindromes are between 10,000 and 998,001
# - There are fewer palindromes than products of 3-digit numbers
# Approach: Look for palindromes and return the first one that has
#   two 3-digit factors

def has3DigitFactors(number):
    for x in range(100, 999)[::-1]:
        for y in range(100, 999)[::-1]:
            if number / x == y:
                print("Factor 1: {}\nFactor 2: {}".format(x, y))
                return True
    return False

for number in range(10000, 998001)[::-1]:
    if str(number) == str(number)[::-1] and has3DigitFactors(number):
        print(number)
        exit()

# Result: 906609 (993 * 913)