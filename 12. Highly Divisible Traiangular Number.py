
def factors(k):
    if k<1:
        raise ValueError("Cannot be less than 1")
    i = 1
    fact = []
    while i*i <= k:
        if k%i == 0:
            fact.append(i)
            if i != k//i:
                fact.append(k//i)
        i +=1
    return fact



def divisible_triangular(m):
    if m<1:
        raise ValueError('Cannot be less than 1')
    i = 1
    j=2
    while len(factors(i)) <= m:
        i +=j
        j +=1
    return i

# print(divisible_triangular(500))

print(factors(15))