#read elements into list
#user_input=input("enter the elements to sort")
#sor_list=[]
#sor_list=list(map(int,user_input.split(" ")))
sor_list=[64, 34, 25, 12, 22, 11, 90, 5]
print(sor_list)
#sor_list=map(int,sorlist)
#bubble sort
#swap the higher element to the right
# so in each  iteration the largest number is placed in the right side
n=len(sor_list)
for i in range(0,n):
    for j in range (0,n-i-1):#doing an n+1 for j , hence we need to do n-1,-i as last element is sorted
        if (sor_list[j]>sor_list[j+1]):
            sor_list[j],sor_list[j+1]=sor_list[j+1],sor_list[j]
print(sor_list)