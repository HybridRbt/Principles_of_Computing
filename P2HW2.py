__author__ = 'jeredyang'

"""
Q5
"""

count = 0

def memoized_fib(num, memo_dict):
    global count
    count += 1
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

for n in range(21):
    print ""
    print n
    print memoized_fib(n, {0: 0, 1: 1})
    print count
