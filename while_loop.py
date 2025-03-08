# i = 1
# while i <= 1_000:
#   print(i)
#   i = i + 1

# i = 1
# while i <= 10:
#   print(i * '*')
#   i = i + 1


# # Example while loop:
# x = 0
# while x < 5:
#   print("Not there yet, x=" + str(x))
#   x = x + 1
# print("x=" + str(x))



# # Another example while loop:
# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")
    
# attempts(5)

# Question
# In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?
# 
# def count_down(start_number):
#   while (current > 0):
#     print(current)
#     current -= 1
#   print("Zero!")

# count_down(3)


# Solution:
# def count_down(start_number):
#   current = start_number
#   while (current > 0):
#     print(current)
#     current -= 1
#   print("Zero!")

# count_down(3)



	# this is an infinite loop:
# def countNumbers(start_number):
#     current = start_number
#     while(current > 0):
#        print(current)
#        current += 1
#        print("infinite")

# countNumbers(1)     




# Question:
# Reflect
# The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?
# def print_range(start, end):
# 	# Loop through the numbers from start to end
# 	x = start
# 	while x <= end:
# 		print(x)

# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)



# the problem here is that x is not being incremented anywhere making the condition endlessly true. I needed to add x += 1 or x = X + 1 for the incrementation to tell it to add a new number until it gets to the end.





# Solution:
# def print_range(start, end):
# 	# Loop through the numbers infinitely
# 	x = start
# 	while x <= end:
# 		print(x)
# 		x += 1 # or x = x + 1 

# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)



# Ex while loop
# multiplier = 2
# result = multiplier * 4
# while result <= 100:
#     print(result)
#     multiplier += 1
#     result = multiplier * 4
# print("Finished")


# This while loop prints the multiples of 4 between 2 and 100. The
# "multiplier" variable is initialized with the starting value of 2. 
# The "result" variable is initialized with the value of the 
# "multiplier" variable times 4. 

# The while loop specifies that the loop must iterate while it is True
# that the "result" is less than or equal to 100. Within the while loop, 
# the code tells the Python interpreter to print the value of the 
# "result" variable. Then, the "multiplier" is incremented by 1 and the
# "result" is assigned the new value of the "multiplier" times 4. 

# The end of the while loop is indicated by the indentation of the next 
# line of code moving one tab to the left. At this point, the Python
# interpreter automatically loops back to the beginning of the while
# loop to check the condition again with the new value of the "result"
# variable. When the while loop condition becomes False (meaning
# "result" is no longer less than or equal to 100), the interpreter exits
# the loop and reads the next line of code outside of the loop. In this 
# case, that next line tells the interpreter to print the string "Finished". 





# Question:
# The following code contains an infinite loop, meaning the Python interpreter does not know when to exit the loop once the task is complete. To solve the problem, you will need to:

# Find the error in the code

# Fix the while loop so there is an exit condition

# Hint: Try running your function with the number 0 as the input and observe the result.

# Note that Coursera’s code blocks will time out after 5 seconds of running an infinite loop. If you get this timeout error message, it means the infinite loop has not been fixed. 
# 
def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number % 2 == 0:
    number = number / 2
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  
# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False






# Solution
def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number > 1 and number % 2 == 0:
    number = number / 2
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  
# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False




# Question:
# Write a function that takes an argument n and returns the sum of integers from 1 to n. For example, if n=5, your function should add up 1+2+3+4+5 and return 15. If n is less than 1, just return 0. Use a while loop to calculate this sum. 
# 
def sum_of_integers(n):
  if n < 1:
    return 0


  # i = 1
  # sum = ___
  # while ___:
  #   sum = sum + i
  #   i = ___


  return sum


print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15
















# Solution: 
def sum_of_integers(n):
  if n < 1:
    return 0


  i = 1
  sum = 0
  while i <= n:
    sum = sum + i
    i = i + 1


  return sum


print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15




# 5.
# Question 5
# Fill in the blanks to complete the function, which should output a multiplication table. The function accepts a variable “number” through its parameters. This “number” variable should be multiplied by the numbers 1 through 5, and printed in a format similar to “1x6=6” (“number” x “multiplier” = “result”). The code should also limit the “result” to not exceed 25. To satisfy these conditions, you will need to:

# Initialize the “multiplier" variable with the starting value

# Complete the while loop condition

# Add an exit point for the loop

# Increment the “multiplier" variable inside the while loop
# 
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 0


    # Complete the while loop condition.
    while number <= 25:
        result = number * multiplier 
        if  result > 25:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        number += 1



multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15


multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25


multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24        



# Solution
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1


    # Complete the while loop condition.
    while number <= 25:
        result = number * multiplier 
        if  result > 25:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier = multiplier + 1