from math import pi
import cmath as c

# TODO: use the naive way for small instances

def dft(a, inverse=False, first=True):
    ''' Performs discrete Fourier transform. '''
    # append 0 until len(a) is not a power of two
    if first:
        pw = 1
        while pw < len(a):
            pw <<= 1
        a = a + [0] * (pw - len(a))

    n = len(a)
    if n == 1:
        return a

    w_n, w = c.exp((-1 if inverse else 1) * pi * 2j / n), 1
    a_hat = [0 for _ in range(n)]
    a_hat_0 = dft(list(a[::2]), inverse=inverse, first=False)
    a_hat_1 = dft(list(a[1::2]), inverse=inverse, first=False)

    for k in range(n >> 1):
        a_hat[k] = a_hat_0[k] + w * a_hat_1[k]
        a_hat[k + (n >> 1)] = a_hat_0[k] - w * a_hat_1[k]
        w = w * w_n
    return a_hat

def idft(a):
    ''' Performs inverse discrete fourier transform. '''
    n = len(a)
    return list(map(lambda x: x/n, dft(a, inverse=True)))

def multiply(p, q):
    '''
        Multiplies two polynomials with real coefficients:
            p = [p_0, p_1, ...]
            q = [q_0, q_1, ...]
    '''
    n = max(len(p), len(q))
    p += [0] * (2*n - len(p))
    q += [0] * (2*n - len(q))

    p_hat, q_hat = dft(p), dft(q)
    pq_hat = [p_hat[i] * q_hat[i] for i in range(len(p_hat))]
    return list(map(lambda x: round(x.real, 3), idft(pq_hat)))

if __name__ == "__main__":
    print_poly = lambda pl: print(*['{:+.0f}x^{:d}'.format(pl[i], i) for i in range(len(pl)-1,-1,-1) if pl[i]])
    p, q = [1, 2, 0, 8], [0, -1, 0, 0, 12]
    print('Polynomials p, q:')
    print_poly(p)
    print_poly(q)
    print('Polynomial p*q:')
    print_poly(multiply(p, q))

    from time import clock
    n, start = 100000, clock()
    p = [i&1 for i in range(n)]
    multiply(p, p)
    print('Multiplying polynomial p*p of length {:d} takes {:.3f} s.'.format(n, clock()-start))
