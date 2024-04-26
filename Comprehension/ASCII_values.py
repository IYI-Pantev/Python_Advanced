from timeit import default_timer as timer

start = timer()
list_of_characters = ['N', 'i', 'c', 'k']

ascii_dict = {c: ord(c) for c in list_of_characters}
print(ascii_dict)
end = timer()
print(end - start)