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