#if else statement
a=100
b=20
if a<b:
    print("less")
elif a==b:
    print("equal")
else:
    print("greater")

# one line if statement
if a>b:print("a is greater than b") # single line if statement
print("a is bigger ") if a>b else print("b is bigger")

# while statement
i =1
'''while i < 6 :
    print(i)
    i+=1'''
# while with break statement and continue statement
i =1
'''while i < 6 :
    print("continue after two , breaks at    3",i)
    i += 1
    if i==1:
      continue
    if i==3:
     break'''
# while can be used with else statement as well

#for statement
#for x in range(0,4):
#    print(x)

lista=["red","orange","yellow","green"]
listb=[1,2,3,4]
'''for x in lista:
    for y in listb:
        print(x,y)'''
#lambda expression- more like a small anonymous function
# can take in many parameters but can only perform one expression
x=lambda a,b,c:a*b+c
print(x(10,20,30))
# utility of  lambdafunction  within a function

def lambda_example(a):
    return lambda n:a*n
res1=lambda_example(5) #
print(res1(20))

