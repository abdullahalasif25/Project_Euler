
def prime(k):
    if k<2:
        return False
    if k ==2:
        return True
    if k%2 == 0:
        return False

    i = 3
    while i*i <=k:
        if k%i == 0:
            return False
        i +=2
    return True


    
def sum_of_primes(n):
    total = 0
    for i in range(2, n):
        if prime(i):
            total +=i
    return total

print(sum_of_primes(2000000))