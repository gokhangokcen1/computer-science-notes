def race(x,y):
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

print(race(5, 7))
print(race(2, 4))


print("---------------FIZZ BUZZ----------")
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print( "fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


print(fizzbuzz(16))



print("---------------IS PRIME?----------")

def is_prime(n):
    if n == 1: 
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(10))
print(is_prime(7))
print(is_prime(1))


print("---------------UNIQUE DIGITS----------")
def unique_digits(n):
    """Return the number of unique digits in positive integer n."""
    unique = []
    for digit in str(n):
        if not has_digit(unique, digit):
            unique.append(digit)
    return len(unique)

def has_digit (n,k):
    """Returns whether k is a digit in n."""
    return str(k) in str(n) 

print("unique_digits ex.")
print(unique_digits(8675309))
print(unique_digits(13173131))
print(unique_digits(101))
print("has_digit ex")
print(has_digit(10, 1))
print(has_digit(12, 7))


print("---------------ORDERED DIGITS----------")

def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing order, and False otherwise"""
    digits = str(x)
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True

print(ordered_digits(5))
print(ordered_digits(11))
print(ordered_digits(127))
print(ordered_digits(1357))
print(ordered_digits(21))









