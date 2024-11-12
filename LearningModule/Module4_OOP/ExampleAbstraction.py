#data abstraction
#to hide uneccesary info/code details from the user
# using __variablename or __variablename_
#it makes it difficutl to access - mangling
#python re writes it as _classname__variablename
#helps to avoid naming conflicts between parent class and child class
class ExampleAbstraction:
    def __init__(self, side):
        self.__side=side# here __side referes to private variable
    def get_side(self):
        return self.__side
    def get_area(self):
        return self.__side*self.__side
    def get_perimeter(self):
        return 4*self.__side

#create object
ea_obj= ExampleAbstraction(5)
print(ea_obj.get_area())
print(ea_obj.get_perimeter())
#this is to access the private variable through getmethod
print(ea_obj.get_side())
#this is to access the private variable through mangling - _classname__variablename
print(ea_obj._ExampleAbstraction__side)
