'''Basic class and object definition and declartion'''

class Animal:
    '''A simple Animal class'''

    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    
    def bark(self):
        return f"{self.name} is Making sound "

anml = Animal("Suman","Pink")
print(anml.bark())

