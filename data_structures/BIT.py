# fenwick tree
class Bit:
    def __init__(self, n):
        sz = 1
        while n >= sz:
            sz *= 2
        self.size = sz
        self.data = [0 for _ in range(sz)]

    def sum(self, i):
        assert i > 0
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        assert i > 0
        while i < self.size:
            self.data[i] += x
            i += i & -i

# Range Fenwick tree
class RangeBit:
    def __init__(self, n):
        sz = 1
        while n >= sz:
            sz *= 2
        self.size = sz
        self.dataAdd = [0 for _ in range(sz)]
        self.dataMul = [0 for _ in range(sz)]

    def sum(self, i):
        assert i > 0
        add = 0
        mul = 0
        start = i
        while i > 0:
            add += self.dataAdd[i]
            mul += self.dataMul[i]
            i -= i & -i
        return mul * start + add

    def add(self, left, right, by):
        assert 0 < left <= right
        self._add(left, by, -by * (left - 1))
        self._add(right, -by, by * right)

    def _add(self, i, mul, add):
        assert i > 0
        while i < self.size:
            self.dataAdd[i] += add
            self.dataMul[i] += mul
            i += i & -i
