age = 20

match age:
    case _ if age < 18:
        print("Minor")
    case _ if age < 65:
        print("Adult")
    case _:
        print("Senior")
