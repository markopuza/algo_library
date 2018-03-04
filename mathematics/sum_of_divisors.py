def modified_prime_list(n):
    ''' Modified primes list sieve. '''
    prime = [False, False] + [True for _ in range(n)]
    for i in range(2,int(n ** 0.5) + 1):
        if prime[i] == True:
            for j in range(i, n // i + 1):
                prime[i * j] = i # composite numbers have this entry
    return prime

def sum_of_divisors(n):
    ''' The sum of divisors list for numbers <= n, uses multiplicativeness. '''
    sod, p = [0 for _ in range(n + 1)], modified_prime_list(n)

    # resolve prime powers
    for i in range(2, n + 1):
        if p[i] == True:
            pw, exp = i, 2
            while pw <= n:
                sod[pw] = (i ** exp - 1) // (i - 1)
                pw *= i
                exp += 1

    # fill in composite numbers using multiplicativeness
    for i in range(2, n+1):
        if sod[i] == 0:
            pw = p[i]
            num = i // p[i]
            while num % p[i] == 0:
                pw *= p[i]
                num //= p[i]
            sod[i] = sod[pw] * sod[num]

    # get rid of improper divisors
    for i in range(2, n + 1):
        sod[i] -= i

    return sod

if __name__ == "__main__":
    print(sum_of_divisors(20))
    s = sum_of_divisors(1000)
    assert s[s[284]] == 284
    assert s[s[220]] == 220
    print('Tests passed.')
