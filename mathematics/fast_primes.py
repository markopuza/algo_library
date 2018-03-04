from pyprimesieve import primes

if __name__ == "__main__":
    from time import clock
    start = clock()
    lim = 5*10**8
    n = len(primes(lim))
    print('    There are {:d} primes < {:d}. This took {:.3f} s.'.format(n, lim, clock()-start))
