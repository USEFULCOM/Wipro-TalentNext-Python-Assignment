import string

# --- Assignment 1 (Lambda): Cube every number in a list --- #
print("--- Assignment 1: Lambda Cubes ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubes = list(map(lambda x: x**3, numbers))
print(f"Original list: {numbers}")
print(f"Cubed list: {cubes}")
print("-" * 30 + "\n")


# --- Assignment 2 (List Comp): Dictionary of odd numbers and their cubes --- #
print("--- Assignment 2: Dictionary of Odd Cubes ---")
input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {num: num**3 for num in input_list if num % 2 != 0}
print(f"Input List: {input_list}")
print(f"Output Dictionary: {output_dict}")
print("-" * 30 + "\n")


# --- Assignment 3 (List Comp): Dictionary of alphabets and integers --- #
print("--- Assignment 3: Alphabet Dictionary ---")
alphabet_dict = {char: index + 1 for index, char in enumerate(string.ascii_lowercase)}
print("Alphabet to Integer Mapping:")
print(alphabet_dict)
print("-" * 30 + "\n")