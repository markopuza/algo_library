def memoize(f):
    ''' memoization decorator '''
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)
# the above is good, but not for recursion


# the below template is fast
##############################


import sys
sys.setrecursionlimit(10000) # improve limit

memo = {}
def f(a):
    # base cases
    if a <= 1:
        return a
    # memoization step
    if a in memo:
        return memo[a]
    ret = memo[a] = f(a-1) + f(a-2) # recursive expression
    return ret

for _ in range(int(input())):
    print(f(int(input())))
