class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        print( self.name, self.age)        

a1 = Animal("lion", 23) 
a2 = Animal("cat", 32)
a1.speak()
a2.speak()

        


