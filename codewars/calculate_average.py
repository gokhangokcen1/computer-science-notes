def find_average(numbers):
    # your code here
    if len(numbers) != 0:
        sum = 0
        numbers_length = len(numbers)
        for number in numbers:
            sum += number
        return sum / numbers_length
    else:
        return 0
