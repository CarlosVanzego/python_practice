# This line opens the file spider.txt in read mode. The open() function returns a file object which is assigned to the variable file.
file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read)
file.close()


# These lines print the first three lines of the file. The readline() method reads one line from the file and returns it as a string. The read() method reads the entire file and returns it as a string. The close() method closes the file.
file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()
with open("spider.txt") as file:
  print(file.readline())



# Q: Code snippet that will correctly open a file and print lines one by one without whitespace?
with open("hello_world.txt") as text:
    for line in text:
	    print(line.strip())






