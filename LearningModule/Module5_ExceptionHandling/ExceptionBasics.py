# Intro to exception handling
#try: code that cause exception
#except: code to run when exception occurs

#example 1 division by zero, basic try,except

nume=12
deno=0
try:
    print(nume/deno)
except:
    print("cannot divide by zero")
#example 2  taking input from user,  try and except with specific errors
try:
    temp=int(input("please enter a number"))
    print (temp)
except ValueError:
    print("expected number , found value other than number")


