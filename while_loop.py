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
def countNumbers(start_number):
    current = start_number
    while(current > 0):
       print(current)
       current += 1
       print("infinite")

countNumbers(1)     




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
def print_range(start, end):
	# Loop through the numbers infinitely
	x = start
	while x <= end:
		print(x)
		x += 1 # or x = x + 1 

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)





