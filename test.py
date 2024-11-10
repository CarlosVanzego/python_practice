def factorial(n):
   if n == 0:
      return 1
   else: 
      return n * factorial(n-1)
   
   number = int(input("Enter a number: "))
   result = factorial(number)
   print("The factorial of {} is {}.format(number, result)")

# Defines a function called factorial: This function takes a number n as input and recursively calculates its factorial.
# Gets input from the user: It prompts the user to enter a number.
# Calculates the factorial: It calls the factorial function to calculate the factorial of the entered number.
# Prints the result: It displays the result to the user.
