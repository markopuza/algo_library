class min_heap:
    '''
    Min heap with array storage
    '''
    def __init__(self):
        self.arr = []
        self.size = 0

    def __str__(self):
        return str(self.arr)

    def get_min(self):
        if self.size > 0:
            return self.arr[0]

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def parent(self, i):
        return (i - 1) >> 1

    def bubble_up(self, i):
        curr = i
        while curr > 0:
            par = self.parent(curr)
            if self.arr[curr] < self.arr[par]:
                self.arr[curr], self.arr[par] = self.arr[par], self.arr[curr]
                curr = par
            else:
                break

    def heapify(self, i):
        curr = i
        while self.left_child(curr) < self.size:
            left, right = self.left_child(curr), self.right_child(curr)
            if right >= self.size or self.arr[left] <= self.arr[right]:
                chil = left
            else:
                chil = right

            if self.arr[curr] > self.arr[chil]:
                self.arr[curr], self.arr[chil] = self.arr[chil], self.arr[curr]
                curr = chil
            else:
                break

    # add element
    def add(self, v):
        self.arr.append(v)
        self.bubble_up(self.size)
        self.size += 1

    # remove element
    def delete(self, v):
        i = self.arr.index(v)
        if i == self.size - 1:
            self.arr.pop()
            self.size -= 1
            return
        self.arr[i] = self.arr.pop()
        self.size -= 1
        self.bubble_up(i)
        self.heapify(i)

class max_heap:
    '''
    Max heap using min_heap with negative numbers
    '''
    def __init__(self):
        self.minh = min_heap()

    def __str__(self):
        return str(list(map(lambda x: -x, self.minh.arr)))

    def get_max(self):
        return -self.min.get_min

    def add(self, v):
        self.minh.add(-v)

    def delete(self, v):
        self.minh.delete(-v)

# MIN HEAP with custom comparator

class min_heap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def __str__(self):
        return str(self.arr)

    def get_min(self):
        if self.size > 0:
            return self.arr[0]

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def parent(self, i):
        return (i - 1) >> 1

    def less(self, seg1, seg2):
        # define comparator

    def bubble_up(self, i):
        curr = i
        while curr > 0:
            par = self.parent(curr)
            if self.less(self.arr[curr], self.arr[par]):
                self.arr[curr], self.arr[par] = self.arr[par], self.arr[curr]
                curr = par
            else:
                break

    def heapify(self, i):
        curr = i
        while self.left_child(curr) < self.size:
            left, right = self.left_child(curr), self.right_child(curr)
            if right >= self.size or self.less(self.arr[left], self.arr[right]):
                chil = left
            else:
                chil = right

            if not self.less(self.arr[curr], self.arr[chil]):
                self.arr[curr], self.arr[chil] = self.arr[chil], self.arr[curr]
                curr = chil
            else:
                break

    def add(self, v):
        self.arr.append(v)
        self.bubble_up(self.size)
        self.size += 1

    def delete(self, v):
        i = self.arr.index(v)
        if i == self.size - 1:
            self.arr.pop()
            self.size -= 1
            return
        self.arr[i] = self.arr.pop()
        self.size -= 1
        self.bubble_up(i)
        self.heapify(i)



def test():
    h1, h2 = min_heap(), max_heap()
    for n in [4,3,6,1,3,4,3]:
        h1.add(n)
        h2.add(n)
    print(h1,h2)
    h1.delete(1)
    print(h1)
    h2.delete(6)
    print(h2)
    h2.delete(4)
    print(h2)
    h2.delete(4)
    print(h2)
# test()
