

def multiple(n):
    m = []
    i = 1
    while i * i < n:
        if n%i == 0:
            if i not in m:
                m.append(i)
                m.append(n//i)
        i +=1
    return m

def prime(k):
    if k>2:
        i = 2
        while i* i <= k:
            if k%i == 0:
                return False  
            i +=1
        return True
    elif k ==2:
        return True
    else:
        return False


def largest_prime_factor(l):
    multiples = multiple(l)
    return max(i for i in multiples if prime(i))
    
print(largest_prime_factor(600851475143))