# create class dnode

class DNode:

    def __init__(self,data,prev,next):
        self.data=data
        self.prev=prev
        self.next=next

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def addElements(self,data):
        if self.head == None:
            self.head=DNode(data,None,None)
            #print(self.head.data)
        else:
         itr=self.head

         while itr.next != None:
              itr=itr.next

         itr.next=DNode(data,itr,None)
    def addListOfElements(self,datalist):
        self.head=DNode(datalist[0],None,datalist[1])
        dlen= len(datalist)
        itr=self.head
        for i in range(1,dlen-2): #5,10,15
           itr.next= DNode(datalist[i],itr,datalist[i+1])
           itr=itr.next
        itr.next= DNode(datalist[dlen-1],itr,None)
    def printElements(self):
        itr=self.head
        if itr.next == None:
            print(itr.data)
        else:
            while itr.next != None:
                print(itr.data)
                itr=itr.next
            print(itr.data)#to print the last element
    def printElementsReverse(self):
        itr=self.head
        if itr.next==None:
            print(itr.data)
        else:
            while itr.next!= None:
                itr=itr.next
        # we have traversed till the end of th list
        #now we use prev to print it in reverse
        while itr.prev != None:
            print(itr.data)
            itr=itr.prev
        print(itr.data)

if __name__ =='__main__' :
        ddl=DoublyLinkedList()
        ddl.head=None
       # ddl.addElements(5)
        #ddl.addElements(10)
        #ddl.addElements(15)
        #ddl.addElements(20)
        #ddl.addElements(25)
        ddl.addListOfElements([5,10,15,20,25,30])
        ddl.printElements()
        ddl.printElementsReverse()

        #ddl.addElements(10)
        #ddl.addElements(15)
        #ddl.addElements(20)


