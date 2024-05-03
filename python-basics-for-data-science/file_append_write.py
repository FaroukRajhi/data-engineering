
file = open("/home/farouk/python/text.txt", "w")

file.write("Hello from python file with write mode\n")

myFile = open("/home/farouk/python/fun.txt", "w")
myFile.write("Hello from school\n" * 10)

myList = ["Farouk","Rajhi","devops"]
myFile = open("/home/farouk/python/fun.txt", "a")
myFile.write("Hello from blaze\n" * 10)
myFile.writelines(myList)
myFile.write("Hello from blaze\n" * 10)

file.close()
myFile.truncate(5)
# = There are several methods 