import math

def prime(l):
    if l > 2:
        i = 2
        while i*i <= l:
            if l%i == 0:
                return False
            i +=1
        return True
    elif l ==2:
        return True
    else: 
        return False

def next_prime(m):
    m = m + 1
    while not prime(m):
        m +=1
    return m



def prime_factors(k):
    i = 2
    factors = []
    while i <=k:
        if k%i == 0:
            factors.append(i)
            k = k//i
        else:
            i = next_prime(i)
    return factors



def smallest_multiple(n):
    prime_set = [ ]
    for i in range(2, n+1):
        factors = prime_factors(i)
        for j in set(factors):
            need = factors.count(j)
            have = prime_set.count(j)
            if have < need:
                prime_set.extend([j] * (need - have))         
    return math.prod(prime_set)

print(smallest_multiple(20))

