# tuples
#ordered and unchangeble
# van be used to store key's - values, or standard values that do not change over time
# example  colors tRed(255,0,0)
t1=('a','b','c','d','e')
print(t1)
#creating tuple with only one element
tOneElement=(1,)
tNotOneElementTuple=(1)
print(tOneElement, "  "+str(type(tOneElement)))
print(tNotOneElementTuple, "  "+str(type(tNotOneElementTuple)))
#accessing tuples
#and indexing starts from 0
print(t1[2:4])# accepts negative ranges
# can use "in" to check if an element exists
if 'a' in t1:
    print('a in t1')

# you can add tuple to another tuple
t2=('x','y','z')
print(t2)
t1+=t2
print(t1)
#note : all the elements are added as individual elements and not as a single tuple elements
# for other tuple updations , convert tuple into list, update it as a list and convert it into tuple
#del is used for deleting a tuple

# packing and unpacking
# packing= assigning values to tuples
#unpacking =assigning a tuple values to a variable
tBool=(0,1)# packing
(vZero,vOne)=tBool
print(vZero,vOne)

# can loop through a tuple using for statement

for i in range(len(tBool)):
    print(i)

#multiplying tuple
tBool=tBool*2
print("multiplied by 2",tBool)# no numerical multiplication but produces output
print("count() method for tuple ",tBool.count(0))# repeated number in tuple
print("index() method for tuple, returns the position for provided val ",tBool.index(1))#




