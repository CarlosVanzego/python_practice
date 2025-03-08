# this function calculates the area of a triangle:
# 
base = 6
height = 4

area = (base*height)/2

# this is a function that does the same thing, and is more reusable:
# 
def area_triangle(base, height):
    return base*height/2


area_a = area_triangle(12, 6)
area_b = area_triangle(14, 3)
sum = area_a + area_b

print("The sum of both areas is: " + str(sum))


# the first operation below is calcuating how many hours are in the given amount of seconds; the second works out how many minutes are left once we subtract the hours; and then how many seconds remain after subtracting the minutes.
# We end up with three numbers as a result; so the function returns all three of them. 
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)

# because we know that the function returns three vlaues, we assign the results of the function to three different variables.




