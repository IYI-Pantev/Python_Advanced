# 1 filtering nums
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# 2 odd nums 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

print(list(odd_numbers))  # Output: [1, 3, 5, 7, 9]

# filtering non-empty stings
strings = ["hello", "", "world", " ", "python", ""]
non_empty_strings = filter(lambda x: x.strip() != "", strings)

print(list(non_empty_strings))  # Output: ['hello', 'world', 'python']

# 3 filtering nested lists
nested_lists = [[1, 2, 3], [], [4, 5], [6], [], [7, 8, 9]]
non_empty_lists = map(lambda x: len(x) > 0, nested_lists)

print(list(non_empty_lists))  # Output: [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
