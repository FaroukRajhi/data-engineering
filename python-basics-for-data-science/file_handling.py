# "a" Append
# "r" Read
# "w" write
# "x" create

# variable = open(file absolute path,mode) function

# import os
# 
# print(os.getcwd())
# print(os.path.abspath(__file__)) # __file__ this current python file
# print(os.path.dirname(os.path.abspath(__file__)))
file = open(r"/home/farouk/python/text.txt", "r")
# print(file) # File data object
# print(file.read())
# print(file.readline(1))
# print(file.readlines())

for line in file:
    
    if line == "devops":
        continue
    print(line)
