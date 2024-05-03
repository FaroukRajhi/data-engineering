"""
Every object has:
- A type
- An internal data representation
- A set of procedures of interacting with the object (method)
"""

# Create a class: circle

"""
def __init__(self,radius, color):
    self.radius = radius
    self.color = color
"""

class Phone:

    def __init__(self,model,color):

        self.model = model
        self.color = color



    def Model(self):
        return "your favorite model is: " ,self.model
    
    def Color(self):
        return "your favorite color is: ",self.color

# Create a instance of a class


Model_1 = input("Enter a model name: ")
Color_2 = input("Enter a color value: ")
phone_1 = Phone(Model_1,Color_2)
print(phone_1.Model())
print(phone_1.Color())