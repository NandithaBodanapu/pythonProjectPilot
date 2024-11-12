#Object oriented concepts
#creating class

class  book:
    #attribute
    book_color="blue"

   #create init method
    def __init__(self,name):
        self.name=name
    def author(self,name):
        self.name=name
        print("the author name is " +self.name)

#object creation
b1=book("Harry Potter")
b2=book("Da vinci code")


print(f"name of the first book : {b1.name}")#calling the method using object
print(f"name of the second book:{b2.name}")
print(f"The color of the book:{b1.book_color}")
print(f"the color " +b2.__class__.book_color)#calling ussing class
b2.author("Dan Brown")




