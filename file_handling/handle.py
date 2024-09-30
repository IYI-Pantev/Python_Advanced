names = open('file_handling/data/names.txt', "+r")

# read(), which returns the entire content
# of the file as a string.
print(type(names.read()))
print(names.read())

names.close()
