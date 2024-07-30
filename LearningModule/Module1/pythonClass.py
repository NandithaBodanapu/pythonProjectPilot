
#class
#class creation
class ex1_class():
    a=20
#object creation for class
ob_ex1=ex1_class()# obj1= classname()
#invoke the class variable with an object
print(ob_ex1.a)

#__init__ function is default function for all class objects

class ex2_caxis():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x},{self.y}"
    def ex2_fun(self):
        print(f"the initial coordinates are ({self.x},{self.y})")
zero_cord=ex2_caxis(0,0)


print(zero_cord.x,zero_cord.y)
print(zero_cord)# to display  the values of x,y using object we need to use by _str_(self)
zero_cord.ex2_fun()#object calling function
# creation of empty class is not permitted
# if you have to create an empty class use pass statement
class empty_class():
    pass

# self is current instance of the class , used to access variable that belong to the class




