from math import sqrt

def prime_list(n):
    '''
    Generates a prime list up to n using the sieve of Eratosthenes
    (inclusive)
    '''
    prime = [False, False] + [True for _ in range(n)]
    for i in range(2,int(sqrt(n)) + 1):
        if prime[i]:
            for j in range(i, n // i + 1):
                prime[i * j] = False
    return prime

def primes(n):
    pr = prime_list(n)
    return list(filter(lambda x: pr[x], range(n + 1)))

def test():
    print(primes(199))
    print(prime_list(15))
# test()
