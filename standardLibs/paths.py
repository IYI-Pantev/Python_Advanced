from pathlib import Path

# using double back slash \\
# so \ is read
# Path("C:\\python12\\Lib")
# # we can simplify with RAW strings
# Path(r"C:\python12\Lib")
# # on linux
# Path("usr/local/bin")
# # path that represents the current folder
# Path()
# #home directory of the current user
# Path.home()


path = Path("Python_Advanced/standardLibs")

# print(path.is_file())
# print(path.exists())
print(path.name)
print(path.parent)
print(path.absolute())
