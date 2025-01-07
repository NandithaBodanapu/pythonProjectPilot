#ref https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md
#create tree as follows, print only uptp the level specified
#global
#   india
#        Gujarat
#            Ahmedhabad
#            Baroda
#        Karnataka
#           banglore
#           Mysore
#   USA
#       new jersey
#            Preinceton
#            trenton
#        california
#            sanfrancisco
#            mountainview
#            palo alto


class treeNodeEx2:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def addChild(self,child):
        child.parent=self
        self.children.append(child)

    def level_ex2(self):
        level=0
        temp=self.parent
        while temp:
            level+=1
            temp=temp.parent
        return level





    def printEx2(self,level):
        if  self.level_ex2()> level:
            return
        print(self.data)
        if self.children:
            for child in self.children:
                child.printEx2(level)

def createTree():

    glb = treeNodeEx2("Global")

    ind=treeNodeEx2("India")
    us=treeNodeEx2("USA")

    guju=treeNodeEx2("Gujarat")
    kar=treeNodeEx2("Karnataka")

    ahem = treeNodeEx2("Ahmedhabad")
    bar = treeNodeEx2("Baroda")

    bang = treeNodeEx2("Banglore")
    mysore = treeNodeEx2("Mysore")

    nj = treeNodeEx2("New Jersey")
    cali = treeNodeEx2("California")

    pri = treeNodeEx2("Princeton")
    tren = treeNodeEx2("Trenton")

    sf= treeNodeEx2("San Francisco")
    mv = treeNodeEx2("Mountain View")
    pa = treeNodeEx2("Palo Alto")
    cali.addChild(sf)
    cali.addChild(mv)
    cali.addChild(pa)
    nj.addChild(pri)
    nj.addChild(tren)
    us.addChild(cali)
    us.addChild(nj)
    guju.addChild(ahem)
    guju.addChild(bar)
    kar.addChild(bang)
    kar.addChild(mysore)
    ind.addChild(guju)
    ind.addChild(kar)
    glb.addChild(ind)
    glb.addChild(us)
    return glb
if __name__ =="__main__":

    tr=createTree()
    tr.printEx2(4)




