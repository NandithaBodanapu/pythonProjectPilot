# selection sort
# finds the lowest values in the array and moves it to the front of the array

sort_arr= [64, 34, 25, 5, 22, 11, 90, 12]
n=len(sort_arr)
minval=0
minindex=0
print(sort_arr)
for i in range(0,n):
    minval=sort_arr[i]
    minindex=i
    for j in range (i+1,n):
        if (minval>sort_arr[j]):
            minval=sort_arr[j]
            minindex=j
    #i have minval and its location
    #pop the min value at its location
    # insert the min value at the begining of the list
    if i!=minindex:
     sort_arr.pop(minindex)
     sort_arr.insert(i,minval)

print(sort_arr)

#in the above code the insertion and poping will cause additional time complexity
#so to instead of inserting and popping we can swap the elements
