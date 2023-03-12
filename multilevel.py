class Parent:
  def __init__(self,name):
    self.name=name
  def getName(self):
    return self.name

class child(Parent):
  def __init__(self,name,age):
    Parent. __init__(self,name)
    self.age=age
  def getAge(self):
    return self.age

class grandchild(child):
  def __init__(self,name,age,location):
    child.__init__(self,name,age)
    self.location=location
  def getlocation(self):
    return self.location

gc=grandchild("RAMESH",24,"HYDERABAD")
print(gc.getName(),gc.getAge(),gc.getlocation())



  
