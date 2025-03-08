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
def count_down(start_number):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)


# Solution:
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)