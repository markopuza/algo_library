# Fast modular inverses of 1...n modulo M
M = 1000000007
modinv = [-1 for _ in range(n + 1)]
modinv[1] = 1
for x in range(2, n + 1):
    modinv[x] = (-(M//x) * modinv[M%x])%M


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

def test():
    print(modinv(2, 5)) # 3
    print(modinv(3, 10)) # 7
    print(modinv(12123, 234233249)) # 162724773
# test()
