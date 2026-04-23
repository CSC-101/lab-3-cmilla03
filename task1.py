more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step.  order = [2,3,4,5]
print(more)     # What is the value of more at this point? more = [2,3,4,5]

def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and. [1,2,3,4]
                                           # the corresponding return value. [1,4,9,16]


squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print(squares)                                    # values recorded above? [1,4,9,16] each value in squares is the return value from calling square(n) on each n in order

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. n = o,1,2,3,4 return values = False, False, False, True, True


answer = [x for x in range(5) if check(x)]   # What is the value of answer? answer = [3, 4]
print(answer)


def inc(m: int) -> int:
    return m + 1  # Record, in order of the calls, each value of m and
    # the corresponding return value. For inc/check:
    # m = 3, 4
    # inc return values = 4, 5
    # n = 0, 1, 2, 3, 4


def check(n: int) -> bool:
    return n > 2  # Record, in order of the calls, each value of n and
    # the corresponding return value. check return values = False, False, False, True, True


answer = [inc(x) for x in range(5) if check(x)]  # What is the value of answer? answer = [4, 5]
print(answer)

