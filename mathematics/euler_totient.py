import primes

def totients(n):
    '''
    Generates the phi array of Euler's totient function
    up to n, using sieving method
    '''
    prime = primes.prime_list(n)
    phi = [float(i) for i in range(n+1)]
    for p in range(2, n+1):
        if prime[p]:
            j = 1
            while j * p <= n:
                phi[p * j] *= 1.0 - 1.0 / p
                j += 1
    return list(map(round,phi))

def test():
    print(totients(100))
# test()
