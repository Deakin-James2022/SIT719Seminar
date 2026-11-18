# Please write a python function to calculate the factorial of a number.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
# Call function
number = 5
print("Factorial of", number, "is:", factorial(number))
