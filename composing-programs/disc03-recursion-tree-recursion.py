print("--------------Q1:MULTIPLY--------------")
def multiply(m,n):
    """Takes two positive integers and returns their product using recursion."""
    # multiply(5,3)
    # 15
    if n == 0:
        return 0
    else:
        return m + multiply(m, n-1)

print(multiply(5,3))
print(multiply(7,4))


print("--------------Q2:SWIPE------------")

def swipe(n):
    """Print the digits of n, one per line, first backward then forward.
    swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    number = n


    if number < 10:
        print(int(n))
    else:
        print(number % 10)
        swipe(number // 10)
    
    if n == 0:
        return 
    print(n % 10) 
    
swipe(2837)



def yazdir(n):

    def print_reverse(n):
        print(n % 10)
        if n > 0:
            
