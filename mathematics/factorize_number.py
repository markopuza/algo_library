def primes(n):
    primfac, d = [], 2
    #factors repeated
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

if __name__ == "__main__":
    print('Prime factorizations:')
    for i in range(50):
        print('    {:d}  ->  {:s}'.format(i, str(primes(i))))
