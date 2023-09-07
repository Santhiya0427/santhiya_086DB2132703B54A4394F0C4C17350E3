# Python 3 program to find
# factorial of given number
def factorial(n):

  # single line to find factorial
  return 1 if (n == 0 or n == 1) else n * factorial(n - 1)


# Driver Code
number = int(input("Enter a value"))

print("Factorial of", number, "is", factorial(number))
