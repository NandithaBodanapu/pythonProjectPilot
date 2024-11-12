class parentclass():
    def __init__(self):
        print("entered parent init class")
    def MethodOne(self,str1):
        print("parent method one called, enterd string is"+str1)
    def MethodTwo(self,str2):
        print("parent method two called, entered string is "+str2)
class childclass(parentclass):
    def __init__(self):
        print("entered child init class")
    def MethodOne(self,str1):
        print("child method one called,entered string is "+ str1)

#creating an object for child class

child1=childclass()
child1.MethodOne("Mary")
child1.MethodTwo("Lamb")