try:
    with open("app.py") as file:
        print('file opened')
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Enter valid age.")
