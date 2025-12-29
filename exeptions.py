# exeptions = events detected during exexution that interrupts the flow of a program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("This will always execute")