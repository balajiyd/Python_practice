numbers_str = input("Enter a list of numbers separated by spaces: ")
numbers_list = numbers_str.split()  # Splits the string into a list of strings
numbers_list = [int(num) for num in numbers_list]  # Converts strings to integers
print(numbers_list)
