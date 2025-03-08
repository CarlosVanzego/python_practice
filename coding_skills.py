# Skill Group 1
# Use a function that accepts multiple parameters
# Return a result value
# 
# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
# 
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(3,6,24))



# Skill Group 2
# Use a function to return the result of a measurement conversion
# Use arithmetic operators to perform a calculation
# Combine text with a function call within a print() statement
# Convert the return value from a float data type to a string for the print() function
# Call the function and perform a calculation on the return value within a print() statement
# 
# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in milliliters is " + str(convert_volume(4)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in milliliters is " + str(convert_volume(2)*3))
# Alternative calculation:
# print("The volume in milliliters is " + str(convert_volume(4))




# Conditionals:
# Skill Group 1
# Use a comparison operator with numbers
# Use a comparison operator to alphabetize strings
# 
# The value of 10*4 (40) is greater than 14+23 (37), therefore this 
# comparison expression will return the Boolean value of True.


print(10*4 > 14+23) # Should print True

# The letter "t" has a Unicode value of 116 and the letter "s" has a
# Unicode value of 115. Since 116 is not less than 115, the 
# comparison of "tall" < "short" (or 116 < 115) is False. 

print("tall" < "short")  # Should print False

# Skill Group 2
# Use a function with the def() keyword
# Pass a parameter to the function
# Use an if-elif-else statement
# Assign strings to variables 
# Use conditional operators
# Return a value
# 
