# Easy If Statement
a, b= 5, 2
if a > b:
    print("It's working!")

# List
name_list=["abc", "def", "ghi"]
name1, name2, name3=name_list
print(name1)
print(name2)
print(name3)

# Joining First and Last Name
fname, lname= "Rajat", "Balyan"
print(fname, lname)
print(fname + lname)

x= "global_variable"
def myFun():
    x="local_variable"
    print(x)

myFun()
print(x)

# Parameter and Argument Test

def type_test(test_num): #test_num -> Parameter
    print(test_num)

type_test("test_1")
type_test("test_2")

# List names of your friends

def friends_list(*friend_name): #friend_name -> Argument
    print("Your friends are " + friend_name[2])

friends_list("good friend", "best friend", "faltu friend")

# For Loop Try

def for_try(data):
    for x in data:
        print(x)

data_list =["data 1", "data 2", "data 3"]

for_try(data_list)

#Lamda Practice

lam_var= lambda n1, n2 : n1 + n2
print(lam_var(5,2))

# Class & Object
class MyClass:
    class_var1= 10
    class_var2="Class Variable"

MyObject = MyClass()
print(MyObject.class_var2)
print(MyObject.class_var1)

# Inheritance

class inherit_parent_class:
    def __init__ (self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)

class inherit_child_class(inherit_parent_class):
    pass

object_of_icc = inherit_child_class("Inheritance", "Done")
object_of_icc.print_name()

# When __init__ function is put inside the child class, it will no longer will inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# super() function will make the child class inherit all the methods and properties from its parent.

class child_class(inherit_parent_class):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.currentyear = year

    def welcome_msg(self):
        print("Welcome", self.firstname, self. lastname, " to start your journey from ", self.currentyear)

obj_of_cc = child_class("Rajat", "Balyan", 2023)
obj_of_cc.welcome_msg()

# Iterators
# iter() method is used to get an iterator

# print("")
# print("Iterators")
print("")

mytuple1 = ("Item 1", "Item 2", "Item 3")
myit1 = iter(mytuple1)

print (next (myit1))
print (next (myit1))
print (next (myit1))

mystr1 = "Banana"
myit2 = iter(mystr1)

# Method 1
print (next(myit2))
print (next(myit2))
print (next(myit2))
print (next(myit2))
print (next(myit2))
print (next(myit2))

# Method 2
# for x in mystr1:
#     print (x)

#Method 1 and Method 2, both gives the same output, i.e. prints all the characters of the string

# --- Creating an iterator ---

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

# print("")
# print("Creating an iterator")
print("")

class myNums:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        var1 = self.a
        self.a += 1
        return var1
    
myclass = myNums()
myiter1 = iter(myclass)

print(next(myiter1))
print(next(myiter1))
print(next(myiter1))

#Stop Iteration
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times

print("")

class myNums2:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <=5:
            var2 = self.a
            self.a += 1

            return var2
        else:
            raise StopIteration
        
myclass = myNums2()
myiter2 = iter(myclass)

for var2 in myiter2:
    print(var2)

#Polymorphism
print("\nClass Polymorphism \n")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!!")

car1 = Car("Ford", "Mustang")           #Creating a Car class
boat1 = Boat("Ibiza", "Toruing 20")     #Creating a Boat class
plane1 = Plane('Boeing', '747')         #Creating a Plane class

for rndmvar2 in (car1, boat1, plane1):
    rndmvar2.move()

#Inheritance Class Polymorphism
print("\nInheritance Class Polymorphism \n")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car1(Vehicle):
    pass

class Boat1(Vehicle):
    def move(self):
        print("Sail!")

class Plane1(Vehicle):
    def move(self):
        print("Fly!")


car2 = Car1("Ford", "Mustang")           #Creating a Car class
boat2 = Boat1("Ibiza", "Toruing 20")     #Creating a Boat class
plane2 = Plane1('Boeing', '747')         #Creating a Plane class

for rndmvar3 in (car2, boat2, plane2):
    print(rndmvar3.brand)
    print(rndmvar3.model)
    rndmvar3.move()

#Func inside another func
print("")

def myFunc1():
    x=100
    def myInnerFunc1():
        print(x)
    myInnerFunc1()

myFunc1()

