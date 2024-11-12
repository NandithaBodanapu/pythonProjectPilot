#polymorphism
#same word many meanings
class parent_vehicles():
    def __init__(self):
        print("parent vehicles init method")
    def tyres(self):
        print("All vehicles have tyres")
    def numberoftyres(self):
        print("there can be 1 to many tyres")

class child_car(parent_vehicles):
    def __init__(self):
        print("This is car init method")
    def numberoftyres(self):
        print("Cars have four tyres")

class child_bike(parent_vehicles):
    def __init__(self):
        print("This is bike init method")
    def numberoftyres(self):
        print("Bikes have two tyres")
#object creation invokes the __init__ method
pv=parent_vehicles()
cc=child_car()
cb=child_bike()
print("")
cc.tyres()# method of parent class
cc.numberoftyres()
print("")
cb.tyres()# method of parent class
cb.numberoftyres()
