

'''
class human:
    def __init__(self,n,o):
        self.name =n
        self.occupation=o

    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots a flim")

    def speaks(self):
        print(self.name,"says how are you?")

a=human("azeem","actor")
a.do_work()
a.speaks()
'''   #creating a class and object with class and instance attributes
'''class dog:
     #class attribute
     atrr = "mammal"

     #instance attribute
     def __init__(self,name):
        self.name = name

    #object instantiation
rodger = dog("rodger")
tommy = dog("tommy")

    #accessing class attributes
print("Rodger is a {}".format(rodger.__class__.atrr))
print("tommy is also a {}".format(tommy.__class__.atrr))

    #accessing instance attributes
print("my name is {}".format(rodger.name))
print("my name is {}".format(tommy.name))''' 
""



























""" 
           #class and object or instance with muslim class(class have properities and methods with object and object call)
class muslim:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o

    def do_work(self):
        if self.occupation=="praying":
            print(self.name,"pray for God")
        elif self.occupation=="enjoyment":
            print(self.name,"enjoyment is for child")
        else:
            print("no option selected")

    def speak(self):
        print(self.name,"says assalamu aleikum")


a=muslim("adfd","adfz")
a.speak()                    
a.do_work() """

             
'''
    #inheritance of vehcile class
  
class vehcile:
    def general_usage(self):
        print("general usage:Transportation")

class car(vehcile):
    def __init__(self):
        print("i am car")
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        print("specific usage:commute to work,vacation with family")


class motorcycle(vehcile):
     def __init__(self):
        print("i am motorcycle")
        self.wheels=2
        self.has_roof=False

     def specific_usage(self):
        print("specific usage:Road trip,racing")


c=car()
c.general_usage()
c.specific_usage() 

m=motorcycle()
m.general_usage()
m.specific_usage()
'''
   

'''
   # Multiple inheritance
class father():
    def skills(self):
        print("father enjoy gardening,programming")

class mother():
    def skills(self):
        print("mother love cooking,art")

class child(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)     
        print("I like hardworking,learning new things")


c=child()
c.skills()'''                       
