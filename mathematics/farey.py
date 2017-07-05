def farey(n, lim = 1):
    ''' generates the terms of Farey sequence F_n up to number <= lim '''
    F = [(0, 1), (1, n)]
    while 1:
        (a, b), (c, d) = F[-2], F[-1]
        p = int((n + b) / d) * c - a
        q = int((n + b) / d) * d - b
        if (p / q) <= lim:
            F.append((p, q))
        else:
            break
    return F

def test():
    for i in range(1, 8):
        print(farey(i))
    print(farey(7, 4/7))

test()
