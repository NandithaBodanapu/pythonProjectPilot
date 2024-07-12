# contains strings, Boolean , Operatorss
#strings
# either single quotation or double quotation
#to display we need to use print("")
multiline="""this is a multiline
assignment operator"""
print(multiline)
print("Array")
#strings are arrays represented by [] , indexing starts at 0
str_array="jack"
print(str_array[0])
print(str_array[1])
print("for loop")
#looping through string, FOR loop

#for x in str_array:
#    print(x)
for st in "abc":
    print(st)
print("length")
print("the length of abc is " +str(len("abc"))) # to print we need to convert the length into string type

#if statement, in statement and not in statemnt
#in and not in are case sensitive
lineOne="this is a line"
print(lineOne)
if "abc" not in lineOne:
    print("abc not in line")
if "this" in lineOne:
    print("this in line")
if "IS" not in lineOne:# case sensitive
    print("IS is not present in line")
#slicing  name[startindex:endindex], index starts at 0
slice_example="abcdefghijk"
print(slice_example)
print(slice_example[0:2]) # will print n-1 digits
print(slice_example[:4])# from begining upto 4
print(slice_example[5:])# from 5 till end
print(slice_example[-5:-3])# counts from the end
#str.upper()
#str.lower()
#str.strip()
#str3=str1+str2 // + for concatenation
# fstring formating string

x=12
txt= f"i am in{x} grade"
print (txt)

rs=80
# :.2f to format it to two decimal points
txt = f"the price of dollar 5 in indian currency is {5 * rs:.2f}"
print(txt)
#boolean values
# any string, number ,tuple,dict,list and set- are all true unless empty or number=0

#python operators

#python identity operator - same object and same memory location
#is ,is not
#python membership operator
# in , not in

