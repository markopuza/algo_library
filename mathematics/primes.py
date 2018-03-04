
def prime_list(n):
    ''' Generates a primality list up to n using the sieve of Eratosthenes (inclusive). '''
    prime = [False, False] + [True for _ in range(n)]
    for i in range(2,int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i, n // i + 1):
                prime[i * j] = False
    return prime

def primes(n):
    ''' Generates a list to primes up to n (inclusive). '''
    pr = prime_list(n)
    return list(filter(lambda x: pr[x], range(n + 1)))

if __name__ == "__main__":
    n = 50
    print('Lists of primes up to {:d}:'.format(n))
    print('   {:s}'.format(', '.join(map(str, prime_list(n)))))
    print('')
    print('   {:s}'.format(', '.join(map(str, primes(n)))))
