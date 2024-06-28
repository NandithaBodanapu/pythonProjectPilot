#learning reference from w3school
# this file contains basic syntax for python programming language
# single line comment

print("hello world")
# variable assignment- no such command directly assign variable
x_number=4
y_string="abc"
print(type(x_number))# type is for getting the data type

# variable names- case sensitive, (a-z,A-z,0-9,_),name must start with alphabet or _ (not number)
# assigning multiple values in a single line
a,b,c="first", "second","third"
print(a)
print(b)
print(c)
# the multiple variable single ,same value
p=q=r= "same value"
print(p,q,r)
print(p+" "+q+" "+r)# string displays as it is
print(x_number+x_number)# number it adds

# global keyword
g= "global value"# as its declared outside its global by default
# the global value can be changed in the local scope by defining it as global and updating it
#data types
#text - str
#numeric- int, float, complex
#sequence - list,tuple,range
#mapping - dict
#set - set,frozenset
#boolean- bool
#binarytypes -bytes , bytearray, memoryview
#nonetype- NoneType

#python number -{int , float, complex}
print(float(10))
print(int(11.11))
print(complex(3))






