class Person:
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname

    def myfunc(self):
       print(self.fname, self.lname )

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome",self.fname,self.lname,"to the class of", self.graduation_year)
    
p1 = Student("virat", "kohli",2023)
p1.welcome()
















