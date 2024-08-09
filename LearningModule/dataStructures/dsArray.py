#reference
#https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures
# python only has dynamic array
# size of
# int is 4
#char is 1
#float is 4
#array complexity time
#display a particular index -O(1) as we are just identifying the index
#search -O(n)- search all elements using for loop
#display all elements-O(n) using for loop
#insertion/deletion value - (index,val) at O(n)

'''Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
'''
#ex1 start
''' 
#create a list to store values
monthlyList=list()
monthlyList.append(list(("January",2200)))
monthlyList.append(list(("February", 2350)))
monthlyList.append(list(("March",2600)))
monthlyList.append(list(("April", 2130)))
monthlyList.append(list(("May", 2190)))

#1. In Feb, how many dollars you spent extra compare to January?
tempJan=0
tempFeb=0
for i in monthlyList:
    if i[0]=="January":
        tempJan=i[1]
    if i[0]=="February":
        tempFeb=i[1]

print(f"extra dollars spent:  {tempFeb-tempJan}")
#print(monthlyList)
#2. Find out your total expense in first quarter (first three months) of the year.
quater=0
for i in monthlyList[0:3]:
    quater=quater + i[1]

print(f"the total expense of first quater {quater}")

#3. Find out if you spent exactly 2000 dollars in any month
for i in monthlyList:
    if i[1]==2000:
        print(f"spent 2000 in {i[0]}")

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthlyList.append(list(("June",1980)))
print(monthlyList)
##5.You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this
monthlyList[3][1]=monthlyList[3][1]+200
print(monthlyList)
#ex1 end
'''
#ex2
'''You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
'''
#ex2 start
'''
heros = ['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
print(f"the length of heroes is {len(heros)}")
#2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
print(heros)
loc_hulk=heros.index('hulk')
heros.insert(loc_hulk+1,"black panther")
print(heros)
#4 So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#Do that with one line of code.
heros.remove('thor')
heros.remove('hulk')
print(heros)
heros.append('doctor strange')
print(heros)
heros.sort()
print(heros)
'''
#ex2 end
#ex3
'''Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
Solution'''

#print("enter the max number")
max_num=int(input("enter the max number"))
for i in range(1, max_num):
 if i%2 != 0:
  print(i)


