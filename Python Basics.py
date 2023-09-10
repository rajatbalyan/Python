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

