from random import randrange

def find_kth(arr, k, start=0, end=None):
    '''
        Finds k-th smallest element in the array arr.
         *Assumes UNIQUE elements in the array*
         Runs in expected time O(n).
    '''
    if not end:
        end = len(arr) -1
    pivot_ridx = randrange(start, end)
    pivot = arr[pivot_ridx]
    pivot_idx = _partition(arr, start, end, pivot_ridx)
    if pivot_idx + 1 == k:
        return pivot
    elif pivot_idx + 1 > k:
        return find_kth(arr, k, start, pivot_idx)
    else:
        return find_kth(arr, k, pivot_idx, end)

def _partition(arr, start, end, pivot_idx):
    pivot = arr[pivot_idx]
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
    inc_idx = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[inc_idx], arr[i] = arr[i], arr[inc_idx]
            inc_idx += 1
    arr[end], arr[inc_idx] = arr[inc_idx], arr[end]
    return inc_idx

if __name__ == "__main__":
    from random import shuffle, randint
    from time import clock
    for l in range(1, 7):
        arr = list(range(1, 10**l))
        k = randint(1, len(arr))
        shuffle(arr)

        start = clock()
        assert k == find_kth(arr, k)
        print('{:d}-th element in array of length {:d} found in {:.3f}'.format(k, 10**l, clock() - start))

        start = clock()
        for a in arr:
            _ = a
        print('    Pure iteration takes {:.3f}'.format(clock() - start))
