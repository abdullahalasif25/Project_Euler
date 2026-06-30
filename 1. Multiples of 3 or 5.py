
# def multiples(a, b):
#     Values = { a: [], b :[], a*b: []}

#     for key, value in Values.items():
#         x=1
#         while key*x  < 1000:
#             value.append(key*x)
#             x +=1
            
#     return sum(Values[a]) + sum(Values[b]) -sum(Values[a*b])


def multiples(a,b):
    return sum(i for i in range(1000) if i%a==0 or i%b==0)




print(multiples(3,5))