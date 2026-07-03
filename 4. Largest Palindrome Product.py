
def palindrome(n):
    return n == int(str(n)[::-1])
    


def multiple_of_digit(n, start, end):
    
    for i in range(start, end, -1 ):
        if n%i == 0:
            other = n//i
            if end <= other <= start:
                return True
    return False
            
            

def largest_palindrome(digit):
    if digit >=1:
        start = int(str(9)*digit)
        end = 10**(digit-1)
        
        for test in range(start * start, end*end-1, -1):
            if palindrome(test) and multiple_of_digit(test, start, end):
                return test
            
    else:
        print("digit must be greater than or equal to 1")
        return None
             

print(largest_palindrome(3))