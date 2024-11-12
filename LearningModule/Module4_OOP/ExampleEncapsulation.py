#encapsulation
#wrapping data and variables in one unit, one basic feature of oop
# class does that , the variable and methods are withing the scope of class
#advantages dosent allow accidental changes to the variables and methods withing the class

class Parent_en():
    def __init__(self):
        self.val_a=3
class child_en(Parent_en):
    def __init__(self):
        Parent_en.__init__(self)
        print("child_en(parent_en) : ", self.val_a)
        self.val_a=33
        print("child_en :", self.val_a)
p1=Parent_en()
c1=child_en()

print("Accessing with parent object", p1.val_a )
print("Accessing with child  object", c1.val_a )

#the variable values remain same

