# i = 1
# while i <= 1_000:
#   print(i)
#   i = i + 1

# i = 1
# while i <= 10:
#   print(i * '*')
#   i = i + 1


# Example while loop:
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))



# Another example while loop:
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)

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
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)



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
def print_range(start, end):
	# Loop through the numbers from start to end
	x = start
	while x <= end:
		print(x)

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)



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
multiplier = 2
result = multiplier * 4
while result <= 100:
    print(result)
    multiplier += 1
    result = multiplier * 4
print("Finished")


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





