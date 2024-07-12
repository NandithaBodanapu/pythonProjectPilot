#multiple items in single variable
# no order
# existing values cannot be changed , new values can be added or existing values can be deleted
# no duplicate values
# can contain heterogeneous elements
#Exception - 1 and true are same
#Exception -0 and false are same
setA = {1, 2, 3, 4, 5}
print(setA)

setB = set(('q', 'r', 's', 't'))  # creating a set using constructor, order may change
print(setB)
# add
# adding an element
setB.add('z')
print(setB)
# adding another set, use update
setB.update(setA)
print(setB)
# adding an iterable example list, use update
listA = ['listOne', 'listTwo']
setB.update(listA)
print(setB)
print(type(setB))

setC = {'q', 'r', 's', 't'}  # creating a set using constructor still creates it randomly
print(setC)

# removing set items
setC.remove('t')  # it item does not exist it will throw error
print(setC)
setC.discard('a')  # if item not there it wont throw an error
print(setC)
print(setC.pop())  # pop remove element randomly
print(setC)
#clear , clears the set
#del deletes the set

#Join
setQ = {1, 2, 3}
setR = {4, 5, 6}
setS = {7, 8, 9}
setT = {1, 4, 7}
setU = {'a', 'b'}
#union
setUn1 = setQ.union(setR)
print(setUn1)
setUn2 = setQ | setU | setS  # union operator
print(setUn2)
#update , changes the original set
setU.update(setQ)
print(setU)
#setQ.intersection(setT)# common values, &operator
print(setQ.intersection(setT))
# the values that are not common,-operator
#note: it displays the values of R that are not there in T, does not display the elements of T that are not there in R
print(setR.difference(setT))  # the values that are not common,-operator
print(setR.symmetric_difference(setT))  # it displays values both in R and T
