#Binary tree has 2 nodes atmost
#bfs=breadth first search
#dfs=depth first search - in order traversal

#logn is search process
# binary search tree does not have duplicates
#implementation

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def addChild(self,data):
        if data ==self.data:
            # do not add any data
            return
        if data<self.data:#add it to the left side
            if self.left:#check if self.left is present
                self.left.addChild(data)
            else:# if no left is present make a new node and add it to left
                self.left=BinaryTreeNode(data)

        if data>self.data:
            if self.right:# recursively call the add child function by pointing the self to the right node
                self.right.addChild(data)
            else:#has no node on right side , just add the data as a new node
                self.right=BinaryTreeNode(data)
            #add it to the right side


    def inOrderTraversal(self): # go left,root, right
        values=list()
        if self.left:
            values.append(self.left.inOrderTraversal())
        values.append(self.data)

        if self.right:
            values.append(self.right.inOrderTraversal())

        return values


    def buildTreeFromInput(self,values):
        rootnode=BinaryTreeNode(values[0])
        for i in range(1,len(values)):
            rootnode.addChild(values[i])
        return rootnode




