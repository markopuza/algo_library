from math import sqrt

def isPrime(n):
   """
    http://mathworld.wolfram.com/StrongPseudoprime.html
   Zhang (2001, 2002, 2005, 2006, 2007) conjectured that
   """
   firstPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]
   lpow = pow
   if n >= 10**36:
      # w = range(2, int(2*log(n)**2)) # pour etre deterministe, ERH dependent !!!
      # (log 2)-1 log n log log n.
      logn = log(n)
      w = range(2, int(logn*log(logn)/log(2)) ) # meilleure borne, conjecture !!!

   elif n >= 1543267864443420616877677640751301: w = firstPrime[:20]
   #elif n >= 1543267864443420616877677640751301: w = firstPrime[:19]
   elif n >= 564132928021909221014087501701: w = firstPrime[:18]
   #elif n >= 564132928021909221014087501701: w = firstPrime[:17]
   elif n >= 59276361075595573263446330101: w = firstPrime[:16]
   elif n >= 6003094289670105800312596501: w = firstPrime[:15]
   elif n >= 3317044064679887385961981: w = firstPrime[:14]
   elif n >= 318665857834031151167461: w = firstPrime[:13]
   elif n >= 3825123056546413051: w = firstPrime[:12]#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
   elif n >= 341550071728321: w = firstPrime[:9]#[2, 3, 5, 7, 11, 13, 17, 19, 23]
   elif n >= 3474749660383: w = firstPrime[:7]#[2, 3, 5, 7, 11, 13, 17]
   elif n >= 2152302898749: w = firstPrime[:6]#[2, 3, 5, 7, 11, 13]
   elif n >= 4759123141: w = firstPrime[:5]#[2, 3, 5, 7, 11]
   elif n >= 9006403: w = [2, 7, 61]
   elif n >= 489997:
      if n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17 and n%19\
      and n%23 and n%29 and n%31 and n%37 and n%41 and n%43 and n%47\
      and n%53 and n%59 and n%61 and n%67 and n%71 and n%73 and n%79\
      and n%83 and n%89 and n%97 and n%101:
         # Fermat 2, 3, 5, special remix
         hn = n>>1
         nm1 = n-1
         p = lpow(2, hn, n)
         if (p==1 or p==nm1):
            p = lpow(3, hn, n)
            if (p==1 or p==nm1):
               p = lpow(5, hn, n)
               return (p==1 or p==nm1)
      return False
   elif n>=42799:
      # Fermat 2, 5
      return (n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17\
      and n%19 and n%23 and n%29 and n%31 and n%37 and n%41 and n%43\
      and lpow(2, n-1, n)==1 and lpow(5, n-1, n)==1) != 0
   elif n>=841:
      # Fermat 2
      return (n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17\
      and n%19 and n%23 and n%29 and n%31 and n%37 and n%41 and n%43\
      and n%47 and n%53 and n%59 and n%61 and n%67 and n%71 and n%73\
      and n%79 and n%83 and n%89 and n%97 and n%101 and n%103\
      and lpow(2, n-1, n)==1) != 0
   elif n>=25:
       # divisions seules
      return (n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17 and n%19 and n%23) != 0
   elif n>=4:
      return (n&1 and n%3) != 0
   else:
      return (n>1) != 0

   if not(n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17\
   and n%19 and n%23 and n%29 and n%31 and n%37 and n%41 and n%43\
   and n%47 and n%53 and n%59 and n%61 and n%67 and n%71 and n%73\
   and n%79 and n%83 and n%89): return False

   # Miller-Rabin
   s = 0
   d = n-1
   while not d&1:
      d>>=1
      s+=1
   for p in w:
      x = lpow(p, d, n)
      if x == 1: continue
      for _ in range(s):
         if x+1 == n: break
         x = x*x%n
      else: return False
   return True

def is_prime(n):
      '''
      Determines primality (quite) efficiently
      '''
      if n <= 1:
            return False
      if n <= 3:
            return True
      if n % 2 == 0 or n % 3 == 0:
            return False
      for i in range(6, round(sqrt(n)) + 2, 6):
            if n % (i - 1) == 0 or n % (i + 1) == 0:
                  return False
      return True

def test():
      print(list(filter(is_prime,range(100))))
# test()
