# difference between return and print 

def welcome():
    print('Go')
    return 'hello'

def cal():
    print('Bears')
    return 'world'

# welcome()
# Go
# 'hello'

# print(welcome(), cal())
# Go
# Bears
# hello world 

# NOTE: print first, return last 
print("--------------------------------------------")
# What if? 

def ab(c,d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')

ab(10,20)
# 10 
# foo 


def bake(cake,make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make 

bake(0,29)
# 1
# 29

bake(1, "mashed potatoes")
# mashed potatoes



print("--------------------------------------------")


def falling(n,k):
    """Compute the falling factorial of n to depth k."""
    if k == 0:
        return 1
    total = 1
    for i in range(k):
        total = total * ( n - i)
    return total

print(falling(6,3))
print(falling(4,3))
print(falling(4,1))
print(falling(4,0))









