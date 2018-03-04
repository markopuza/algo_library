def farey(n, lim = 1):
    ''' Generates the first terms of Farey sequence F_n up to number <= lim. '''
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

if __name__ == "__main__":
    from fractions import Fraction
    for i in range(1, 8):
        print('    Farey sequence F_{:d}:\n         {:s}'.format(\
            i, ', '.join(list(map(lambda x: str(Fraction(*x)), farey(i, 1))))))
