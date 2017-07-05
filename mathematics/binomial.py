def choose(n, k):
    '''
    Computes binomial efficiently
    '''
    if k < 0 or k > n or n < 0:
        return 0

    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result

def test():
    print(choose(1254,611))
# test()
