def fast_modinv(up_to, M):
    ''' Fast modular inverses of 1..up_to   modulo M. '''
    modinv = [-1 for _ in range(up_to + 1)]
    modinv[1] = 1
    for x in range(2, up_to + 1):
        modinv[x] = (-(M//x) * modinv[M%x])%M
    return modinv

def egcd(a, b):
    ''' Extended Euclidian algorithm. '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    ''' Finds modular inverse modulo m. '''
    while a < 0:
        a += m
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

if __name__ == "__main__":
    assert modinv(2, 5) == 3 == fast_modinv(4, 5)[2]
    assert modinv(3, 10) == 7 == fast_modinv(4, 10)[3]
    assert modinv(12123, 234233249) == 162724773 == fast_modinv(200000, 234233249)[12123]
    M = 10**9+7
    MI = fast_modinv(20000, M)
    for i in range(300):
        assert MI[10000+i] == modinv(10000+i, M)
    print('Tests passed.')
