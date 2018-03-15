
def ccw(a, b, c):
    ''' Checks if three points are in counterclockwise order. '''
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

def intersect(a, b, c, d):
    ''' Checks if two *line segments* intersect. '''
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

def intersection(p1, p2, p3, p4):
    ''' Find the intersection point of p1p2 and p3p4. '''
    if not intersect(p1, p2, p3, p4):
        return None
    x1, y1, x2, y2, x3, y3, x4, y4 = *p1, *p2, *p3, *p4
    px = float((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4))
    d = float((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    py = float((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4))
    return (px/d, py/d)

def parallel(a, b, c, d):
    ''' Checks if two lines are parallel. '''
    u = (b[0] - a[0], b[1] - a[1])
    v = (d[0] - c[0], d[1] - c[1])
    return u[0]*v[1] == u[1]*v[0]

from fractions import gcd

def normalize(v):
    ''' Normalizes an integral vector. '''
    g = gcd(abs(v[0]), abs(v[1]))
    v0, v1 = v[0] // g, v[1] // g
    if v0 < 0:
        v0, v1 = -v0, -v1
    elif v0 == 0 and v1 < 0:
        v0, v1 = -v0, -v1
    return((v0, v1))

def shoelace(pol):
    '''
        Shoelace formula for the area of a polygon. O(|V|).
        ! Assumes the vertices of polygon are in SORTED order.
    '''
    n, area = len(pol), 0.0
    for i in range(n):
        j = (i + 1) % n
        area += pol[i][0] * pol[j][1]
        area -= pol[j][0] * pol[i][1]
    return abs(area) / 2.0

from math import atan2

def angle_sort(pts):
    ''' Sorts points by angle, starting from the positive x axis, counterclockwise. '''
    pts.sort(key = lambda b: atan2(-b[1], -b[0]))
    return pts

if __name__ == "__main__":
    pol = [[0, 0], [0, -10], [-10, 0]]
    print('The area of {:s} is {:.3f}'.format(str(pol),shoelace(pol)))

    print('Parallel: ' + str(parallel((1, 0), (0, 1), (-1, 0), (0, -1))))

    vec = (-14, 7)
    print('{:s} normalizes to {:s}'.format(str(vec), str(normalize(vec))))

    print('Intersection: ' + str(intersection((1,1), (-1,-1), (-1, 1), (1, -1))))

    print('Sorted points: ' + str(angle_sort([(1,1), (-1,-1), (-1, 1), (1, -1)])))
