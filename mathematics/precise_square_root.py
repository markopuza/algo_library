def precise_square_root(n, precision):
    a, b = 5 * n, 5
    while len(str(b)) < precision + 5:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = 100 * (b // 10) + 5
    return str(b)[:precision]

def test():
    print(precise_square_root(128937, 100))
# test()
