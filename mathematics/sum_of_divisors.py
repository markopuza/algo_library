from math import sqrt

def prime_list(n):
    '''
    Generates a prime list up to n using the sieve of Eratosthenes
    (inclusive)
    '''
    prime = [False, False] + [True for _ in range(n)]
    for i in range(2,int(sqrt(n)) + 1):
        if prime[i] == True:
            for j in range(i, n // i + 1):
                prime[i * j] = i
    return prime

def sum_of_divisors(n):
    ''' returns the sum of divisors list for numbers <= n ,uses multiplicativeness '''
    sod = [0 for _ in range(n + 1)]
    p = prime_list(n)

    # resolve prime powers
    for i in range(2, n + 1):
        if p[i] == True:
            pw, exp = i, 2
            while pw <= n:
                sod[pw] = (i ** exp - 1) // (i - 1)
                pw *= i
                exp += 1

    # fill in composite numbers using multiplicativeness
    for i in range(2, n+1):
        if sod[i] == 0:
            pw = p[i]
            num = i // p[i]
            while num % p[i] == 0:
                pw *= p[i]
                num //= p[i]
            sod[i] = sod[pw] * sod[num]

    # get rid of improper divisors
    for i in range(2, n + 1):
        sod[i] -= i

    return sod

def test():
    print(sum_of_divisors(20))
    s = sum_of_divisors(1000)
    print('d(284)', s[284])
    print('d(220)', s[220])

test()
