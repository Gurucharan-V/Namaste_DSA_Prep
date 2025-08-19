class Node:
    def __init__(self,val):
        self.val = val
        self.ref = None
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addhead(self,val):
        temp = Node(val)
        temp.ref = self.head
        self.head = temp
        self.size+=1
        
    def addtail(self,val):
        new = Node(val)
        if self.size == 0:
            self.head = new

        temp = self.head
        while temp.ref:
            temp = temp.ref
        temp.ref = new
        
        
    def addindex(self,ind,val):
        new = Node(val)
        temp = self.head
        counter = 0
        
        while counter < ind-1:
            temp = temp.ref
            counter+=1
        new.ref = temp.ref
        temp.ref = new
        
    def getindex(self, ind):
        temp = self.head
        counter = 0
        while counter < ind:
            temp = temp.ref
            counter+=1
        return temp.val
        
        
        
    def printns(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.ref
        
        
a = MyLinkedList()

a.addhead(11)
a.addhead(10)
a.addtail(13)

a.addindex(2,12)


a.printns()

print(a.getindex(0))

