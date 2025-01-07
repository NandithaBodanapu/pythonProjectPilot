#Last in First out
#insert at end
#insert values
# 3 ways to implement stack using python
#list
#collections.deque
#queue .lifoqueue
# using list - dynamic arrays so takes losts of space
#using dqueue  deque internally uses doubly linked list so space is not

# implementing stack as a list

class stackExample:
    def __init__(self):
        pass
    def pushval(self, val, stklist):
        self.val=val
        self.stklist=stklist
        self.stklist.insert(0,val)
    def popval(self,stklist):
        self.stklist=stklist
        self.stklist.pop(0)
    def printvalues(self,stklist):
        self.stklist=stklist
        print(stklist)

se=stackExample()
example=list()
print("inserting at zero and poping elements at zero")
se.pushval(10,example)
se.pushval(20,example)
se.pushval(30,example)
se.pushval(40,example)
se.pushval(50,example)
se.pushval(60,example)
se.printvalues(example)
se.popval(example)
se.printvalues(example)

# using predefined Collections dequeue
from  collections import deque
ex_stack=deque()
ex_stack.append(10)
ex_stack.append(11)
ex_stack.append(12)
print("deque stack", ex_stack )
print(ex_stack.pop())




