def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [x * i for i in range(1, n+1)]

print(count_by(1,10))
print(count_by(2,5))
