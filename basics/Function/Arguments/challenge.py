'''
# Summation Program

**Create a Function** that will accept **N** number of integers as arguments it should get the sum of all integers passed in function and return its sum

**Print of Sum**

**Example**
summation(1,2,3,4,5,6,7,8,9,10)

Output : 55
'''

def summation(*N):
    sum = 0
    for i in N:
        sum += i
    return sum
sum = summation(1,2,3,4,5,6,7,8,9,10)

print(sum)