# sort points by angle, starting from the positive x axis
points.sort(key=lambda b: atan2(-b[1], -b[0]))

def intersection((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
    ''' find the intersection point of X1X2 and X3X3 '''
    px = float((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4))
    d = float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
    py = float((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4))
    return (px/d, py/d)

def normalize(v):
    ''' normalize an integral vector '''
    g = gcd(abs(v[0]), abs(v[1]))
    v0, v1 = v[0] / g, v[1] / g
    if v0 < 0:
        v0, v1 = -v0, -v1
    elif v0 == 0 and v1 < 0:
        v0, v1 = -v0, -v1
    return((v0, v1))

def parallel(a, b, c, d):
    ''' check if two lines are parallel '''
    u = (b[0] - a[0], b[1] - a[1])
    v = (d[0] - c[0], d[1] - c[1])
    return u[0]*v[1] == u[1]*v[0]

def ccw(a, b, c):
    ''' check if points are in counterclockwise order '''
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

def intersect(a, b, c, d):
    ''' check if two *line segments* intersect '''
    return ccw(a,c,d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

def shoelace(p):
    ''' shoelace formula for the area of a polygon '''
    n = len(p)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += p[i][0] * p[j][1]
        area -= p[j][0] * p[i][1]
    return float(abs(area)) / 2.0
