# List comprehensions - concise way to create lists

#For comparison purposes of for loop and LC

# syntax of list comprehension

#[expression for item in iterable if condition]
#expression - the manipulation to be done
#for - keyword
#item in iterable - val/i to temporary store the value of the current list
#if- keyword
#condition- a filtering condition

#example problem: multiply number by self the value of existing list
a=[1,2,3,4,5]
res_for=list()
#solution using for loop
for i in a:
    res_for.append(i*i)
print("using for loop")
print(res_for)
# solution using list comprehension
print("using lc ")
res_lc=[val*val for val in a]
print("example 1 ",res_lc)
res_lc_2=[val*val for val in a if val%2==1]
print("example 2 ",res_lc_2)
# creating list from range
res_lc_3=[val for val in range(0,10)]
print("lc using range:",res_lc_3 )
# creating list of alphabets using range
res_lc_4=[chr(val) for val in range(97,123)]
print("small lettersres",res_lc_4)
res_lc_5=[chr(val) for val in range(65,91)]
print("capital letters",res_lc_5)
# nested loops using lc, all compinations
res_lc_6=[(x,y) for x in range(0,4) for y in range(4,8) ]
print("list of all possible combinations" , res_lc_6)




