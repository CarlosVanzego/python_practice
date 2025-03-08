# def factorial(n):
#    if n == 0:
#       return 1
#    else: 
#       return n * factorial(n-1)
   
#    number = int(input("Enter a number: "))
#    result = factorial(number)
#    print("The factorial of {} is {}.format(number, result)")

# # Defines a function called factorial: This function takes a number n as input and recursively calculates its factorial.
# # Gets input from the user: It prompts the user to enter a number.
# # Calculates the factorial: It calls the factorial function to calculate the factorial of the entered number.
# # Prints the result: It displays the result to the user.





# #  The Coding Cards Practice
# x = 4
# y = "Sally"

# print(type(x), type(y))

# type(5)
# type("Hello")

# vegetables = ["broccoli", "kale", "potato"]
# for x in vegetables:
#    print(x)

# for x in "broccoli":
#    print(x)

# for x in range(6):
#    print(x)

# d = {'x': 1, 'y': 2, 'z': 3}
# for key, value in d.items():
#    print(key, value)



# equation = (2**2) == 4 

# result = equation

# print(result)





# What’s the output of this code if number equals 10?
# number = 10


# if number > 11: 
#   print(0)
# elif number != 10:
#   print(1)
# elif number >= 20 or number < 12:
#   print(2)
# else:
#   print(3)



# Sum
# sum = 4096*2

# print(sum)



# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
# 
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))

number = 4
if number * 4 < 15:
 print(number / 4)
elif number < 5:
 print(number + 3)
else:
 print(number * 2 % 5)