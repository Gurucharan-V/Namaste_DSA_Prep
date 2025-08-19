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
        self.size+=1
        
        
    def addindex(self,ind,val):
        new = Node(val)
        temp = self.head
        counter = 0
        
        if ind == 0:
            self.addhead(val)
            return
        
        while counter < ind-1:
            temp = temp.ref
            counter+=1
        new.ref = temp.ref
        temp.ref = new
        self.size +=1
        
    def getindex(self, ind):
        if ind >= self.size:
            return -1
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
            
    def delnode(self,ind):
        temp = self.head
        counter = 0
        while counter <= ind:
            temp = temp.ref
        print(temp.val)
            
        
            
        
        
a = MyLinkedList()

a.addhead(11)
a.addhead(10)
a.addtail(13)

a.addindex(2,12)
a.addindex(0,9)

a.delnode(3)


a.printns()

# print(a.size)


print(a.getindex(a.size-1))

