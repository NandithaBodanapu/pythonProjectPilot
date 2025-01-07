#tree
#node and edges
#to represent hierarchial data structure
#the child node have a recursive approach
# the child is again a tree
# for a brief understanding of self
# self is an instance of tree node class

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def addchild(self,child):
        child.parent=self# specify the parent as well
        self.children.append(child)# adding a child to the list children

    def get_level_tree (self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent

        print(level)
        return level

    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def exampletree():
    rootnode=TreeNode("root")

    p1node=TreeNode("P1")
    p2node=TreeNode("P2")
    p3node=TreeNode("P3")

    c1node=TreeNode("c1")
    c2node=TreeNode("c2")
    c3node = TreeNode("c3")
    c4node = TreeNode("c4")
    c5node = TreeNode("c5")
    c6node = TreeNode("c6")

    p1node.addchild(c1node)
    p1node.addchild(c2node)

    p2node.addchild(c3node)
    p3node.addchild(c4node)

    p3node.addchild(c5node)
    p3node.addchild(c6node)

    rootnode.addchild(p1node)
    rootnode.addchild(p2node)
    rootnode.addchild(p3node)

    p2node.get_level_tree()
    return rootnode
if __name__=="__main__":

    out=exampletree()
    out.print_tree()
