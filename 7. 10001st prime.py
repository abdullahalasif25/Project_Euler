
def prime(n):
    if n > 2:
        if n%2 == 0:
            return False
        i = 3
        while i*i <= n:
            if n%i == 0:
                return False
            i +=2
        return True
    elif n == 2:
        return True
    else:
        return False



def next_prime(n):
    n +=1
    while not prime(n):
        n +=1
    return n


def nth_prime(n):
    if n<1:
        raise ValueError("n must be at least 1")

    ans = 2
    for _ in range(n-1):
        ans = next_prime(ans)
    return ans 

print(nth_prime(10001))