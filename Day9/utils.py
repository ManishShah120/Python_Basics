def find_max(numbers):
    large = numbers[0]
    for number in numbers:
        if number > large:
            large = number
    return large