mytuple={'a','b','c','d','e'}# tuple creation
myit=iter(mytuple)#creating iterable object

print(next(myit))#printing next iterable object
print(next(myit))
print(next(myit))
print(next(myit))
for x in mytuple:
    print(x)