#create a class node
# a node containes two elements
#data - the number/string
#next- to point to next node
class Node:
    #add a default init function
    def __init__(self, data=None, next=None):# we would be passing arguments
        self.data=data
        self.next=next

#create class linkedlistdemo to prform various functions
class linkedListDemo:
    def __int__(self):# here we wont pass head as an argument, hence we declare it like this
        self.head=None

    def insertAtHead(self,data):
        temp = self.head
        self.head=Node(data,temp)

    def insertAtLoc(self,data,loc):
        itr=self.head

        for i in range(0,loc-2):
            itr=itr.next

        currNode = itr
        itr=itr.next
        curr_next_Node=itr
        #print(currNode.data)
        #print(curr_next_Node.data)
        if curr_next_Node ==None:
           currNode.next=Node(data,None)
        else:

            currNode.next=Node(data,curr_next_Node)

            #curr_next_Node.next=Node(data,currNode)
    def delAtLoc(self,loc):

        itr=self.head
        if loc == 1:
            temp=itr.next
            self.head=temp
        else:
            for i in range(0,loc-2):
                itr=itr.next
            prevElem=itr
            itr=itr.next
            currElem=itr# element to remove
            itr = itr.next  # element after the removed element
            nextElem=itr
            prevElem.next=nextElem
    def addElementAtEnd(self,data):
        # if there are no elements in the linked list
        #self.head=None
        if self.head==None:
           self.head = Node(data,None)
           #print(self.head)
           return
    #if there are elements , we need to iterate to the last element and add the next element over ther
        itr = self.head
        while itr.next :
            itr=itr.next #iterate until the last element

        #itr is the last element in the list
        #itr.next is None as there are no more elements after it
        #so we assign new  element to itr.next
        itr.next=Node(data,None)

    def addListOfElements(self, inlist):
         n=len(inlist)
         if self.head==None:
           self.head =Node(inlist[0],None)
         itr=self.head
         #print(itr.data)
         for i in range(1,n):
             itr.next=Node(inlist[i],None)#set the next val to new node
             itr= itr.next

    def printAllElements(self):
        #print("reached method")
        disp_list=list()
        itr = self.head
        while itr.next:
            disp_list.append(itr.data)
            itr=itr.next
        print(disp_list)
if __name__== '__main__':
    # invoking main method
    lld=linkedListDemo()# creating object for the class
    lld.head=None
    lld.addListOfElements([1,2,3,4,5,6,7])
    #lld.addElementAtEnd(5)
    #lld.addElementAtEnd(25)
    #lld.addElementAtEnd(15)
    #lld.addElementAtEnd(35)
    lld.printAllElements()
    lld.insertAtHead(21)
    lld.printAllElements()
    lld.insertAtLoc(55,3)
    lld.printAllElements()
    lld.delAtLoc(3)
    lld.printAllElements()
    lld.delAtLoc(1)
    lld.printAllElements()