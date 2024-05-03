try..except

try:
  getFile=open("myFile","r")
  getFile.write("File for exception handling")
except IOerror:
  print("Error opening")

else:
