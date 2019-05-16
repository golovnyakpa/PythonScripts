import sympy as np
from fractions import gcd
import random
n1 = 240316804657117
n2 = 240318328671133
p1 = 20791982156839
p2 = 23672587536361
primes = [i for i in np.primerange(5,55)]
def qudratic_modules(primes):
        quadratic = []
        for i in primes:
                temp = []
                for j in range(i):
                        if (j ** 2) % i not in temp:
                                temp.append((j ** 2) % i)
                quadratic.append(temp)
        return quadratic
def factorization(primes, quadratic,n):
        for i in range(int(n ** (1/2))+3):
                flag = 0
                for j in range(len(primes)):
                        if (((n + i ** 2) % primes[j]) in quadratic[j]):
                                flag += 1
                if (flag == len(primes)):
                        if int((n + i ** 2) ** (1/2)) ** 2 == n + i ** 2:
                                j = int((n + i ** 2) ** (1/2))
                                return i, j, i+j, j-i
def ro_pollard(n):
        x = 2
        y = 1
        i = 0
        stage = 2
        x_list = [x]
        while (gcd(n,abs(x-y)) == 1):
                if (i == stage):
                        y = x
                        stage = stage*2
                x = (x*x - 1) % n
                x_list.append(x)
                i = i + 1
        res = gcd(n, abs(x-y))
        return res, n // res, i
quadratic = qudratic_modules(primes)
print(factorization(primes, quadratic,n1), primes)
print(factorization(primes, quadratic,n2),primes)
print(ro_pollard(p1))
print(ro_pollard(p2))
