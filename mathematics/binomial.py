def choose(n, k):
    ''' Computes n choose k.'''
    if k < 0 or k > n or n < 0:
        return 0

    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result

def mod_choose(n, k, M, modinv):
    ''' Given n, k, M and an array modinv of modular inverses,
        Computes n choose k modulo M.
    '''
    if k < 0 or k > n or n < 0:
        return 0

    result = 1
    for i in range(k):
        result *= n - i
        result %= M
        result *= modinv[i + 1]
        result %= M
    return result





if __name__ == "__main__":
    #######################
    # Fast modular inverses of 1...n modulo M
    M = 1000000007
    modinv = [-1 for _ in range(1001)]
    modinv[1] = 1
    for x in range(2, 1001):
        modinv[x] = (-(M//x) * modinv[M%x])%M
    #######################

    for arg in [(5, 0), (0, 5), (5, 5), (132, 22), (123, 34)]:
        r1, r2 = choose(*arg), mod_choose(*arg, M, modinv)
        assert r1 % M == r2
        print('    {:<3d} choose {:<18d} = {:d}'.format(*arg, r1))
        print('    {:<3d} choose {:<3d} mod {:d} = {:d}'.format(*arg, M, r2))
