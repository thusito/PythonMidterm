# Example with a list (mutable)
my_list = [1, 2, 3]
print("Original list:", my_list)

# Change the first element of the list
my_list[0] = 42
print("Modified list:", my_list)

# Example with a string (immutable)
my_string = "hello"
print("Original string:", my_string)

# Attempt to change the first character of the string
try:
    my_string[0] = "H"  # This will raise a TypeError because strings cannot be modified
except TypeError as e:
    print("Error:", e)


