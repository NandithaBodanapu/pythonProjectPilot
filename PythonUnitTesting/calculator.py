class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def add(self,a,b)->float:
        return round(a+b,2)
    def subtract(self,a,b):
        return round(a-b,2)
    def multiply(self,a,b):
        return round(a*b,2)
    def divide(self,a,b):
        if b==0:
            raise ValueError("divide by zero")
        return round(a/b,2)


ob1= calculator()
ob1.add(3,4)