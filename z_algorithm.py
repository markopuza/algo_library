def z_array(s):
    '''
    Computes z-array of string s
    Z-arrays, at index i, stores the length of the longest substring of s
    that starts on i-th place and is also a prefix of s
    '''
    n = len(s)
    z = [n] + [0 for _ in range(n - 1)] # z[0] = n

    # stores the last box window
    left, right = 0, 0
    for k in range(1, n):
        if k > right:
            # compute naively
            cnt = 0
            while cnt + k < n and s[cnt] == s[cnt + k]:
                cnt += 1
            z[k] = cnt
            if cnt > 0:
                left, right = k, cnt + k - 1
        else:
            # we are inside a box, make use of that
            p = k - left # corresponding index in a prefix
            right_part_length = right - k + 1

            # use the past results
            if z[p] < right_part_length:
                z[k] = z[p]
            else:
                # compute naively
                i = right + 1
                while i < n and s[i] == s[i - k]:
                    i += 1
                z[k] = i - k
                left, right = k, i - 1
    return z

def test():
    # https://ivanyu.me/blog/2013/10/15/z-algorithm/
    for s in ['abcxxxabyyy', 'aaaaaa', 'abbbb', 'abcabc', 'abracadabra']:
        print(z_array(s))
# test()
