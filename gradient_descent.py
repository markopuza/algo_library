
def gd(f, df):
    ''' takes function and its derivative '''

    x = [1]

    precision = float(1e-12)
    rate = float(1e-5)
    value = f(*x)

    previous_step = value
    while previous_step > precision:
        next_x = [min(max(0, xi - rate*dxi), s2*50) for (xi, dxi) in zip(x, df(*x))] # restrictions on x

        next_value = f(*next_x)
        previous_step = abs(value - next_value)
        if next_value < value:
            value = next_value
            x = next_x
            rate *= 1.01
        else:
            rate /= 2

    return value


s2 = 2**(0.5)
def f(x):
    return x**2 + 4

def df(x):
    return [2*x]

print(gd(f, df))
