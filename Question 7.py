import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Process each number in the list by its index
for i in range(len(random_numbers)):
    num = random_numbers[i]

    # If the number is greater than 80, replace it with its negative value
    if num > 80:
        random_numbers[i] = -num
    # If the number is lower than 40, replace it with the sum of its digits
    elif num < 40:
        # Convert the number to a string to iterate over each digit
        sum_digits = 0
        for digit in str(num):
            # Convert each digit back to an integer and add to sum_digits
            sum_digits += int(digit)
        random_numbers[i] = sum_digits

# Print the final list after replacements
print(random_numbers)
