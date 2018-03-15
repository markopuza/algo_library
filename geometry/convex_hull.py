
def convex_hull(points):
    '''
        Find convex hull of (unordered) points.
        Andrew's monotone chain algorithm. O(n log n).
    '''
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

if __name__ == "__main__":
    print('The convex hull of 10 x 10 grid is:')
    print(convex_hull([(i//10, i%10) for i in range(100)]))
