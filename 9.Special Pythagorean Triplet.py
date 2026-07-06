

def pythagorean_triplet(total):    
    for a in range(1, total//3):
        for b in range(a+1, (total-a)//2):
            c = total-a-b
            if a**2 + b**2 == c**2:
                return a*b*c
            
    return None

print(pythagorean_triplet(1000))