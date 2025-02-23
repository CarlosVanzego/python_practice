# 5 Tips For Writing Better Code in Python
# 
my_score: int = 0;print(my_score); x: list[str] = ['a', 'b']

print   (        'hello')
# the code above would technically work. however it is hard to read/understand or tell what is going on.
# If you were to reformat this it would look like the example below:
# 
my_score: int = 0
print(my_score)
x: list[str] = ['a', 'b']

print('hello')
# Readability should always come first...

# Tip #2: Prioritize Readability 
# Below is an example of some code that is nearly unreadable; the point of the code is top find the factorial of 10:
# 
def f(n: int) -> int:
  return 1 if n < 2 else (lambda f, n: f(f, n))(lambda f, n: n * f(f, n - 1) if n > 1 else 1, n)

# The code below does the same this but is much more readable, and includes a line that will raise a ValueError should a negative number be entered.
# 
def factorial(number: int) -> int:
    if number < 0:
       raise ValueError("Factorial is not defind for negative numbers.")

    if number == 0 or number == 1:
       return 1

    result: int = 1 
    for i in range(2, number + 1):
       return 1

    result: int = 1
    for i in range(2, number + 1):
       result *= i
    

    return result   
# These two print statements should both show the factorial of 10 (3628800), proving that both of the above code examples work the same way.
print(factorial(10))
print(f(10))



# Tip #3 - Linters
# Linters contirbute to your code running correctly.
# 
my_number: int = 10
print(my_number + 1)

# Tip #4 - Taking advantage of Built-ins
# 



# Tip #5 - Read the Docs/Explore projects on GitHub