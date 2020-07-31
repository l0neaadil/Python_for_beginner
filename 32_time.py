# Calculation of time taken by a function:
from time import time


def timing(func):
    def body(n):                           # n = (*args, **kwargs)
        start = time()
        print('start time of function is: ', start)
        result = func(n)
        end = time()
        print('end time of function is: ', end)
        print("Total time taken: ", end - start)
        print(f'sum of first {n} numbers is: {result}')
    return body


@ timing
def series_sum(n):
    sum_ = 0
    for i in range(n+1):
        sum_ = sum_ + i
    return sum_


series_sum(int(input('enter an ineger: ')))

