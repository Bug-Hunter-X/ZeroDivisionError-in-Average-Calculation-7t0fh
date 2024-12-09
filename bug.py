def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
numbers1 = [10, 20, 30, 40, 50]
average1 = calculate_average(numbers1)
print(f"Average of numbers1: {average1}")

numbers2 = []
average2 = calculate_average(numbers2)
print(f"Average of numbers2: {average2}")

numbers3 = [10, 20, 0, 40, 50]
#The following line is the error, because 0 will be divided and returns ZeroDivisionError
average3 = calculate_average(numbers3)
print(f"Average of numbers3: {average3}")