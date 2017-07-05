
class PriorityQueue:
    ''' class to implement a priority queue
        using simplified version of python's heapq with
        additional functionality (decrease_priority)
        using: https://hg.python.org/cpython/file/2.7/Lib/heapq.py#l242
    '''

    def __init__(self):
        self.heap = []
        self._entryfinder = {}

    def push(self, item, priority):
        self.heap.append((priority, item))
        self._siftdown(0, len(self.heap)-1)

    def cmp_lt(self, x, y):
        # Use __lt__ if available; otherwise, try __le__.
        # In Py3.x, only __lt__ will be called.
        return (x < y) if hasattr(x, '__lt__') else (not y <= x)

    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if self.cmp_lt(newitem, parent):
                self.heap[pos] = parent
                self._entryfinder[parent[1]] = pos
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
        self._entryfinder[newitem[1]] = pos


    def pop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        if not self.heap:
            return None

        lastelt = self.heap.pop()    # raises appropriate IndexError if heap is empty
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self._entryfinder[lastelt[1]] = 0
            self._siftup(0)
        else:
            returnitem = lastelt
        del self._entryfinder[returnitem[1]]
        return returnitem


    def _siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.cmp_lt(self.heap[childpos], self.heap[rightpos]):
                childpos = rightpos
            # Move the smaller child up.
            self._entryfinder[self.heap[childpos][1]] = pos
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[pos] = newitem
        self._entryfinder[newitem[1]] = pos
        self._siftdown(startpos, pos)


    def decrease_priority(self, item, newpriority):
        self.heap[self._entryfinder[item]] = (newpriority, item)
        self._siftdown(0, self._entryfinder[item])

    def is_empty(self):
        return not self.heap
