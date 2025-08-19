class node:
    def __init__(self,val):
        self.val = val
        self.ref = None
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val: int) -> None:
        newnode = node(val)
        newnode.ref = self.head
        self.head = newnode
        self.size+=1

    def addAtTail(self, val: int) -> None:
        newnode = node(val)
        if self.head == None:
            self.head = newnode
            self.size +=1
        else:
            temp = self.head
            while temp.ref:
                temp = temp.ref
            temp.ref = newnode
            self.size +=1
        
    def addAtIndex(self,ind,val):
        temp = self.head
        newnode = node(val)
        counter = 0
        if ind == 0:
            self.head = newnode
            self.size +=1
        else:
            while counter < ind:
                temp = temp.ref
                counter += 1
                
            temp.ref = newnode
            self.size +=1
            

    def printns(self):
        temp = self.head
        
        while temp:
            print(temp.val)
            temp = temp.ref
            
            
a = MyLinkedList()
a.addAtHead(3)
a.addAtTail(5)
a.addAtIndex(1,4)
a.printns()
print(a.size)
