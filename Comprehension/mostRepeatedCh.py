text = 'abc cfg trc oppc hhmnnc'

char_dict = {}
for char in text:
    if char == ' ':
        continue
    char_dict[char] = char_dict.get(char, 0) + 1

# another way for storing char occurrence
char_frequency = {}
for char in text:
    if char == ' ':
        continue

    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1


# print(char_dict)

# 1st way
# max_pair = max(char_dict.items(), key=lambda item: item[1])

# # print(max_pair)

# key, value = max_pair
# print(f"char: {key}: {value} times")

# second way
max_num_value = 0
max_key = ''
for key, value in char_dict.items():
    if value > max_num_value:
        max_num_value = value
        max_key = key
print(f"the most repeated char is \"{max_key}\"\n{max_num_value} times")
