from math import sqrt

def is_square(n):
    '''
    Determines if n is a square efficiently
    '''
    if n < 0 or n % 4 == 3:
        return False
    if n % 2 == 0 and n % 4 != 0:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    if sqrt(n) != round(sqrt(n)):
        return False
    return True

def test():
    for i in range(100):
        print(str(i) + ' ' + str(is_square(i)))
# test()
