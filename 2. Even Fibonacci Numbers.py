
# fibb = [1,2]
# summ= 2
# while (fibb[-1] + fibb[-2]) <4000000:
#     fibb.append(fibb[-1] + fibb[-2])
#     if fibb[-1]%2 == 0:
#         summ += fibb[-1]
#     fibb = [fibb[-2],  fibb[-1]]

# print(summ)
    
    
a = 1
b = 2

summ = 2
while a+b < 4000000:
    a, b = b, a+b
    if b%2 == 0:
        summ +=b

print(summ)