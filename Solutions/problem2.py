# Run time: O(fibonacciSequence(1,N).size())
# Space requirement: O(1)
prev1 = 1
prev2 = 2
sum = 2
done = False

while not done:
    temp = prev1 + prev2
    prev1 = prev2
    prev2 = temp
    if temp > 4000000:
        done = True
    elif temp % 2 == 0:
        sum = sum + temp

print(sum)