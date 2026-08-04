
# def collatz(n):
#     i = 1
#     while n != 1:
#         if n%2 == 0:
#             n = n//2
#         else:
#             n = 3*n + 1
#         i += 1
#     return i

# def largest_collatz(m):
#     maximum = 0
#     while m != 1:
#         n_terms = collatz(m)
#         if n_terms > maximum:
#             maximum = n_terms
#             j = m
#         m -= 1
#     return j

# print(largest_collatz(1000000-1))


def large_collatz(k):
    saved_list = {}
    

    for m in range(k, 1, -1):
        n = m
        i = 0
        while n != 1:
            if n in saved_list:
                i = i + saved_list[n] -1
                break
            else:
                if n%2 == 0:
                    n = n//2
                else:
                    n = 3*n + 1
                i += 1

        saved_list[m] = i+1
    return max(saved_list, key=saved_list.get)

print(large_collatz(1000000))