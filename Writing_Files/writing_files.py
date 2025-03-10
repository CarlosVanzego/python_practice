# The with open() statement creates a file object and assigns it to the variable file. The open() function takes two arguments: the name of the file and the mode. In this case, the mode is w, which means "write". This tells the open() function to create a new file if it doesn't exist, or to overwrite the existing file if it does exist.

# The write() method of the file object takes a string as its argument and writes the string to the file. In this case, the string is "It was a dark and stormy night".
# 
with open("novel.txt", "w") as file:
  file.write("It was a dark and stormy night")