def chinese_remainder(m, a):
    ''' Solves a system of congruences using the C.R.T.
        m - modulos, a - coefficients
        m have to be COPRIME!
    '''
    res = 0
    prod = 1
    for m_i in m:
        prod *= m_i

    for m_i, a_i in zip(m, a):
        p = prod // m_i
        res += a_i * modinv(p, m_i) * p
    return res % prod

def egcd(a, b):
    '''
    Extended Euclidian algorithm
    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    '''
    Finds modular inverse modulo m
    '''
    while a < 0:
        a += m
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

if __name__ == '__main__':
    m = [5, 7, 9, 11]
    a = range(1, 5)
    print(chinese_remainder(m, a))
