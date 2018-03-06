from collections import defaultdict
from fractions import gcd
###########
from sympy.ntheory import factorint

def factorize(n):
    ''' Factorizes number into prime factorization. '''
    primfac, d = defaultdict(int), 2
    #factors repeated
    while d*d <= n:
        while (n % d) == 0:
            primfac[d] += 1
            n //= d
        d += 1
    if n > 1:
       primfac[n] += 1
    return primfac

#### POLLARD'S RHO

def pollards_rho(n, max_iter=100):
    ''' Returns a (hopefully non-trivial) divisor of n. Useful for big numbers. '''
    x, y, d, iters = 2, 2, 1, 0
    f = lambda x: (x*x + 1) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = gcd(abs(x-y), n)
        iters += 1
        if iters > max_iter:
            return n
    return d if d != n else n

if __name__ == "__main__":
    print('Prime factorizations:')
    for i in range(50):
        print('    {:d}  ->  {:s}'.format(i, str(list(factorize(i).items()))))

    print('\nPollard\'s Rho test:')
    from random import randint
    for _ in range(10):
        n = randint(10**30, 10**31)
        divisor = pollards_rho(n)
        print('    {:d} = {:d} x {:d}'.format(n, divisor, n//divisor))
