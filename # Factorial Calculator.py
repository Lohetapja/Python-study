# Factorial Calculator
n = int(input("Enter a number:"))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n <= -1:
       return "Factorial cannot be less then 0"
    else:
        result = 1
        for i in range (1, n + 1):
            result *= i
        return result

result = factorial(n)
print(result)

    