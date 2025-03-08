# it is hard ot determine the purpose of the code below by just looking at it. The names of the variables do not to give the reader much information, and though you can likely work out the result, there is no clue what the result will be used for:
# 
def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)    


# This code below refactored to make the intent of the code above more clear. The names of the variables and the function reflect their purpose, which helps the reader understand the code more quickly.
# 
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)    