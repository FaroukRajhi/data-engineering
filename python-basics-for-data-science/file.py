try:
    file = open("myfile.txt","r")
    file.write("my new file")
except IOError:
    print ("there is no file")