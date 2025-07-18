print("------------------------Q1------------------")
# Q1: A PLUS ABS B

def a_plus_abs_b(a,b):
    """Return a+abs(b), but without calling abs."""
    if b < 0:
        f = lambda x, y: x - b
    else:
        f = lambda x, y: x + b
    return f(a,b)

print(a_plus_abs_b(2,3))
print(a_plus_abs_b(2,-3))
print(a_plus_abs_b(-1,4))
print(a_plus_abs_b(-1,-4))


print("------------------------Q2------------------")
# Q2: HAILSTONE

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length."""
    count = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
        count += 1

    return count
a = hailstone(10)




print("------------------------Q3------------------")
from operator import add, mul 

def square(x):
    return x * x

def identity(x):
    return x

def triple(x):
    return 3 * x

def increment(x):
    return x + 1

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive inteer
    term: a function that takes an index as input and produces a term."""
    result = 1
    for i in range(1, n+1):
        result *= term(i)
    return result

print(product(3, identity))
print(product(5, identity))
print(product(3, square))
print(product(5, square))
print(product(3, increment))
print(product(3, triple))

print("------------------------Q4------------------")
# Q4: Make repeater

def make_repeater(f,n):
    """Returns the function that computes the nth application of f."""
    def iteration(value):
        for _ in range(n):
            value = f(value)
        return value 
    return iteration



add_three = make_repeater(increment, 3)
print(add_three(5)) 
print(make_repeater(triple, 5)(1)) # 3 * 3 * 3 * 3 * 3 * 1
print(make_repeater(square, 2)(5)) # 5^2^2 
print(make_repeater(square, 3)(5)) # 5^2^2^2















