


class Person: # Start a class called"Person"
    def __init__(self,name,age,hobby):  #Start a custom constructor with properties of "name" and "age"
      self.name=name
      self.age=age
      self.hobby=hobby

    def intro(self):  #define a new function called"intro"
        print("My name is",self.name, ",I am",self.age,"years old and my hobby is",self.hobby)

p1=Person('Bob',22,'gaming')  #add object-p1
p2=Person('Amy',25,'reading') #add object-p2

p1.intro() # run function 'intro' with p1
p2.intro() # run function 'intro' with p2