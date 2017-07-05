class SegmentTree:
    # EDIT FOR YOUR QUERIES

    def __init__(self, arr):
        self.set_out_of_bounds()
        self.arr = arr
        self.N = len(self.arr)
        self.tree = [-1 for _ in range(self.N<<2)]
        self.lazy = [0 for _ in range(self.N<<2)]
        self.build_tree(1, 0, self.N - 1)

    def set_out_of_bounds(self):
        self.out_of_bound_value = [0 for _ in range(26)]
    def op(self, a, b):
        return (a + b) % 26
    def qop(self, a, b):
        return [a[i] + b[i] for i in range(26)]

    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) >> 1
            self.build_tree(node<<1, start, mid)
            self.build_tree(node<<1|1, mid + 1, end)
            self.tree[node] = self.op(self.tree[2*node], self.tree[2*node + 1])

    def update_range(self, node, start, end, l, r, val):
        ''' check if the current way to update is ok'''
        if self.lazy[node]:
            self.tree[node] = self.lazy[node]
            #self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node<<1] = self.lazy[node]
                self.lazy[node<<1|1] = self.lazy[node]
                #self.lazy[2*node] += self.lazy[node]
                #self.lazy[2*node+1] += self.lazy[node]
            self.lazy[node] = 0
        if start > end or start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[node] = val
            if start != end:
                self.lazy[node<<1] = val
                self.lazy[node<<1|1] = val
            #self.tree[node] += (end - start + 1) * val
            #if start != end:
            #    lazy[node*2] += val
            #    lazy[node*2 + 1] += val
            return
        mid = (start + end) >> 1
        self.update_range(node<<1, start, mid, l, r, val)
        self.update_range(node<<1|1, mid + 1, end, l, r, val)
        self.tree[node] = self.op(self.tree[node<<1], self.tree[node<<1|1])
        # self.tree[node] = self.tree[node*2] + self.tree[node*2 + 1]

    def query_range(self, node, start, end, l, r):
        if start > end or start > r or end < l:
            return self.out_of_bound_value
            #return 0 # out of range
        if self.lazy[node]:
            self.tree[node] = self.lazy[node]
            if start != end:
                self.lazy[node<<1] = self.lazy[node]
                self.lazy[node<<1|1] = self.lazy[node]
            #self.tree[node] += (end - start + 1) * self.lazy[node]
            #if start != end:
            #    self.lazy[node*2] += self.lazy[node]
            #    self.lazy[node*2 + 1] += self.lazy[node]
            self.lazy[node] = 0
        if start >= l and end <= r:
            return self.tree[node]
        mid = (start + end) >> 1
        p1 = self.query_range(node<<1, start, mid, l, r)
        p2 = self.query_range(node<<1|1, mid + 1, end, l, r)
        #return p1 + p2
        return self.op(p1, p2)

    def update(self, l, r, val):
        ''' inclusive, indexed by 0 '''
        self.update_range(1, 0, self.N - 1, l, r, val)

    def query(self, l, r):
        ''' inclusive, indexed by 0'''
        return self.query_range(1, 0, self.N - 1, l, r)

n, q = map(int, input().split())
arr = list(map(int, input().split()))
st = SegmentTree(arr)
#print(st.tree)
for _ in range(q):
    line = input().split()
    l, r = map(int,line[1:])
    if line[0] == 'q':
        print(st.query(l-1, r-1))
    else:
        st.update(l-1, l-1, r)
#print(st.tree)
#print(st.lazy)
