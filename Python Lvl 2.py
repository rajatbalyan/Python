# Recurcion Practice
def fun_recurcion(var):
    if(var>0):
        result = var + fun_recurcion(var - 1)
        print(result)
    else:
        result=0
    return result

print("Recurcion Reuslts:")
fun_recurcion(10)

#Lambda

print("")
print("Lambda Result")

def fun_lambda(lam_var):
    return lambda lam1 : lam1 * lam_var

num_double= fun_lambda(2)
num_triple= fun_lambda(3)

print(num_double(10))
print(num_triple(10))
print("")

# __init__() function & __str__() function
# REMEMBER: int and str must have double underscores (__)

class class_for_init:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def __str__(self):
        return 

object_for_init = class_for_init("Rajat",19)

print("Name is " + object_for_init.name)
print(object_for_init.age)
