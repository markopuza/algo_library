
def is_square(n):
    ''' Determines if n is a square. '''
    if n < 0 or n % 4 == 3:
        return False
    if n % 2 == 0 and n % 4 != 0:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    SQR = n ** 0.5
    if SQR != round(SQR):
        return False
    return True

if __name__ == "__main__":
    for i in range(101):
        if is_square(i):
            print('{:d} is square.'.format(i))
