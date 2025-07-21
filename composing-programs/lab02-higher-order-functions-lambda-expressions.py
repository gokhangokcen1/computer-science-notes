print("------------------Q1-What whould python display-------")

print(True and 13) # 13
print(False or 0) # 0 
print(not 10) # False
print(not None) # True

#print(True and (1 / 0)) # error
print(True or (1 / 0))  # True
print(-1 and 1 > 0) # True
print(-1 or 5) # -1
print((1 + 1) and 1) # 1

# behaviour:
# AND: if the first one True, return second 
#      if the first one False, return False
# OR : if the first one True, return first
#      if the first one False, return second

def f(x):
    if x == 0:
        return "zero"
    elif x > 0:
        return "positive"
    else:
        return ""

print(0 or f(1)) # False or f(1) -> "positive"
print(f(0) or f(-1)) # "zero" or "" -> True or False -> "zero"
print(f(0) and f(-1)) # "zero" and "" -> True and False -> ""



print("---------------------------Q2-Higher-Order functions------------")

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate = cake() # beets 
# chocolate, returns pie function


print(chocolate) # pie function
print(chocolate()) # sweets, 'cake'
# running pie function

more_chocolate, more_cake = chocolate(), cake # sweets 
# display sweets, keep returned 'cake' and assign this to more_chocolate
# cake function assigned to more_cake

print(more_chocolate) # 'cake'





def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y

print("SNAKE")
print(snake(10, 20)) # 30 
print(snake(10, 20)()) # 

cake = 'cake'
print(snake(10,20))

print("""
      SNAKE
<function cake.<locals>.pie at 0x774ea85acfe0>
sweets
cake
30
""")





print("-----------------------Q3-LAMBDA------------------")

print("""

>>> a = lambda x: x
>>> a(5)
5
>>> b = lambda x, y: lambda: x + y
>>> c = b(8, 4)
>>> c
<function <lambda>.<locals>.<lambda> at 0x77ea8ccbb420>
>>> c()
12
>>> d = lambda f: f(4)
>>> def square(x):
...     return x * x
...
>>> d(square)
16

""")

print("""
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)
type error

>>> higher_order_lambda(g)(2)
4

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
3

>>> print_lambda = lambda z: print(z)
>>> print_lambda
<function <lambda> at >

>>> one_thousand = print_lambda(1000)
10000

>>> one_thousand # nothing

      """)


print("---------------------------Q4-lambdas-and-currying------------------")

def lambda_curry2(func):
    """Returns a curried version of a two-argument function FUNC"""
    return lambda x: lambda y: func(x,y) 


from operator import add, mul, mod
curried_add = lambda_curry2(add)
add_three = curried_add(3)
print(add_three(5))

curried_mul = lambda_curry2(mul)
mul_5 = curried_mul(5)
print(mul_5(42))

print(lambda_curry2(mod)(123)(10))


print("--------------------------Q5-Count-Cond------------------")

def sum_digits(y):
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_fives(n):
    i = 1
    count = 0
    while i <= n:
        if sum_digits(n * i) == 5:
            count += 1
        i += 1
    return count

print(count_fives(10))    # 1
print(count_fives(50))    # 4

def count_primes(n):
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

print(count_primes(6))    # 3
print(count_primes(13))   # 6

def count_cond(condition):
    return lambda n: sum(1 for i in range(1, n + 1) if condition(n, i))

count_fives_func = count_cond(lambda n, i: sum_digits(n * i) == 5)
print(count_fives_func(10))    # 1
print(count_fives_func(50))    # 4

is_i_prime = lambda n, i: is_prime(i)
count_primes_func = count_cond(is_i_prime)
print(count_primes_func(2))    # 1
print(count_primes_func(3))    # 2
print(count_primes_func(4))    # 2
print(count_primes_func(5))    # 3
print(count_primes_func(20))   # 8





