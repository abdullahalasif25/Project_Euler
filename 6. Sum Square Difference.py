
# def sum_square_difference(n):
#     return (n*(n+1)/2)**2 - (n*(n+1)*(2*n+1)/6)





def sum_square_difference(n):
    a = 0
    b = 0
    for i in range(n+1):
        a +=i
        b +=i**2
    return a**2 -b




print(sum_square_difference(10))
