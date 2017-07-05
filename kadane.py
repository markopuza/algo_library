def max_subarray(a):
    '''
    Finds the maximum subarray of array a
    '''
    max_so_far = max_ending_here = 0
    for el in a:
        max_ending_here = max(0, max_ending_here + el)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def test():
    arr = [-1,2,-3,4,-5,5]
    print(max_subarray(arr))
# test()
