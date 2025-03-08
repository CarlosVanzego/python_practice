# Here there are exactly two lines that are the same in the first and second part of the code:
name = "Carlos"
number = len(name) * 9 

print("Hello " + name + ". Your lucky number is " + str(number))

name = "Vanzego"
number = len(name) * 9 

print("Hello " + name + ". Your lucky number is " + str(number))


# when you find code duplication in your scripts, its a good idea to see if you can clean things up by using a function:
def lucky_number(name):
    number = len(name) * 9 
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Carlos")
lucky_number("Vanzego")

