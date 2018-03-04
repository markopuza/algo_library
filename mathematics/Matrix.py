class Matrix:
    ''' Class representing a matrix. '''
    def __init__(self, M):
        self.m = len(M) # rows
        self.n = len(M[0]) # columns
        self.M = M

    def get_rank():
        return (m, n)

    def __getitem__(self, x):
        return self.M[x]

    def __setitem__(self, x, item):
        self.M[x] = item

    def __str__(self):
        return '\n'.join(map(lambda x: ', '.join(map(str, x)), self.M))

    def __repr__(self):
        return self.__str__()

    def transpose(self):
        self.m, self.n = self.n, self.m
        self.M = [list(item) for item in zip(*self.M)]

    def __eq__(self, mat):
        return self.M == mat.M

    def __add__(self, mat):
        assert self.n == mat.n and self.m == mat.m
        res = [[self.M[i][j] + mat.M[i][j] for j in range(self.n)] for i in range(self.m)]
        return Matrix(res)

    def __sub__(self, mat):
        assert self.n == mat.n and self.m == mat.m
        res = [[self.M[i][j] - mat.M[i][j] for j in range(self.n)] for i in range(self.m)]
        return Matrix(res)

    def __mul__(self, mat):
        assert self.n == mat.m
        res = [[0 for _ in range(mat.n)] for _ in range(self.m)]
        for x in range(self.m):
            for y in range(mat.n):
                for k in range(self.n):
                    res[x][y] += self.M[x][k] * mat.M[k][y]

        return Matrix(res)

    def pow(self, exp):
        assert self.n == self.m
        if exp == 0:
            return Matrix([[int(j==i) for j in range(self.n)] for i in range(self.n)])
        if exp == 1:
            return self
        half = self.pow(exp>>1)
        return self.__mul__(half * half) if exp&1 else half * half


if __name__ == "__main__":
    # test via Fibonacci numbers
    fib = [0, 1]
    for _ in range(50):
        fib.append(fib[-1] + fib[-2])

    M = Matrix([[1,0],[1,0]]) + Matrix([[0,1],[0,0]])

    for i in range(1, 30):
        MP = M.pow(i)
        assert MP[0][0] == fib[i+1] and MP[0][1] == MP[1][0] == fib[i] and MP[1][1] == fib[i-1]
    print('Test passed.')
