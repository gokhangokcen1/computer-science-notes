print("--------------------Q1-------------")

result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)
print(result)
# 2 * 3 * 5 = 30 


print("----------------Q5-Digit-Finder-------------")

def find_digit(k):
    """Return a function that return the kth digit of x."""
    assert k > 0 
    def number(num):
        num = str(num)
        if k > len(num):
            return 0 
        else:
            return num[k]
    return number


print(find_digit(2)(3456)) # 5
print(find_digit(2)(5678)) # 7
print(find_digit(1)(10)) # 0 
print(find_digit(4)(789)) # 0



print("----------------Q6-Make-Keeper-------------")

def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integer 1..i..n where calling cond(i) return True."""
    
    def boolean_control(cond):
        for i in range(1, n+1): # takes all valuables
            if cond(i): 
                print(i) # if 
    return boolean_control

def is_even(x):
    return x % 2 == 0


make_keeper(5)(is_even) # 2 4
make_keeper(5)(lambda x: True) # 1 2 3 4 5
make_keeper(5)(lambda x: False) # Nothing is printed



print("----------------Q7-Match-Maker-------------")

def match_k(k):
    """Return a function that checks if digits k apart match."""
    def check(x):
        while x // (10 ** k) > 0:
            if (x % 10) != ((x // (10 **k)) % 10):
                return False
            x //= 10
        return True
    return check

print(match_k(2)(1010)) # True
print(match_k(2)(2010)) # False
print(match_k(1)(1010)) # False
print(match_k(1)(1)) # True
print(match_k(1)(2111111111111111)) # False
print(match_k(3)(123123)) # True
print(match_k(2)(123123)) # False






