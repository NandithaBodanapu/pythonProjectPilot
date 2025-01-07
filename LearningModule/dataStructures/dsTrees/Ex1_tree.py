#exercise 1
from LearningModule.dataStructures.dsTrees.treeExample import TreeNode


#ref  https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md
 #management hierarchy company

#hierarchi structure

#nilpul ceo
# "chinamay cto
#     vishwa  infrastruture header
#         dhaval cloud manager
#         abhijit app manager
#     aamir applications head
# gels hr head
#     peter recruitment manager
#     waqas policy manager

class treeNode:

     def __init__(self,designation,name):
         self.name=name
         self.designation=designation
         self.data=dict({self.designation : self.name})
         self.children=[]
         self.parent=None

     def addChild(self,child):#child is a treenode
        #child=
        child.parent=self
        self.children.append(child)
     def getlevel(self):
         level=0
         temp=self.parent
         while temp:
             level+=1
             temp=temp.parent
         return level

     def displaytree(self):
         cnt=self.getlevel()
         decor=cnt*3*" "+"|__"
         print(decor ,self.name, "("+self.designation+")" )
         if self.children:
            for child in self.children:
                child.displaytree()

     def displaynametree(self):
         cnt=self.getlevel()
         print(" "*3*cnt +"|__", self.name)
         if self.children:
             for child in self.children:
                 child.displaynametree()
     def displaydesignationtree(self):
         cnt=self.getlevel()
         print(" "*3*cnt +"|__", self.designation)
         if self.children:
             for child in self.children:
                 child.displaydesignationtree()
def create_management_tree():

    ceo=treeNode("ceo","Nilpul") #root
    cto=treeNode("cto","chinamay")#p1
    ih=treeNode("infrastructure head","vishwa")#p1c1
    cm=treeNode("cloud manager", "dhaval")#gc1
    am=treeNode("app manager","abhijit")#gc2
    ah=treeNode("applications head","aamir")#p1c2
    hr_head=treeNode("hr_head","gels")#p2
    rm=treeNode("recruitment manager","peter")#c1
    pm=treeNode("policy manager","waqas")#c2

    hr_head.addChild(rm)
    hr_head.addChild(pm)

    ih.addChild(cm)
    ih.addChild(am)

    cto.addChild(ih)
    cto.addChild(ah)

    ceo.addChild(cto)
    ceo.addChild(hr_head)

    return ceo

if __name__== "__main__":
     #obj_tn=TreeNode()
     obj_tn=create_management_tree()
     print("*********PRINTING NAME AND DESIGNATION TREE*****************")
     obj_tn.displaytree()
     print("*******PRINTING NAME TREE*****************")
     obj_tn.displaynametree()
     print("********PRINTING DESIGNATION TREE*****************")
     obj_tn.displaydesignationtree()















