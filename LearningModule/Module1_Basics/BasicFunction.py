# Function a block of code which only runs when its called
#def keyword to create a function
def function_name():
 print("function syntax")

# function call
function_name()
# function with parameter
#parameter defined with the function
#arguments or args are passed as arguments while making a call to the function

def nTable(n):# here n is the parameter
  for i in range(1,11):
   print(i*n)

#nTable(5)#here 5 is an argument, which would replace parameter n in the ntable(function) definition

# can pass multiple arguments
# order does not matter
#for v3, if no explicit value is assigned it will print the default value
#n is a positional argument
#v1,v2 are key arguments
def multipleargs(v1,v2,v3="value3"):
    print("value1 "+v1," value2 "+v2," value3 "+v3)

multipleargs(v2="choclate",v1="biscuit")

#positional only arguments functionname(args,/)
#keyword  arguments functionname(*,args)

def fun_pos(a,b,c,/):
    print(a,b,c)
def fun_keywrd(*,x=10,y=20,z=40):
    print(x,y,z)
fun_pos(100,200,300)
fun_keywrd(x=101)

#using pos and keyword as arguments
def fun_pos_keywrd(p,q,r,/,*,s=11,t=22,u=33):
    print(p,q,r,s,t,u)
fun_pos_keywrd(6,7,8,u=12,t=34)

# can pass list(any iterable as arguments but it has to be extracted accordingly
# return statement
def fun_return(a):
    return a*a
fun_return(5)
# empty function
def fun_empty():
    pass
