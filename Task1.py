#Task 1: Calculate Factorial Using a Function
num = int(input("Enter a Number: "))

def factorial(n):
    if n<2:
        return 1
    return n * factorial(n-1)

print(factorial(num))