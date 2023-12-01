#Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linked_list:
    def __init__(self):
        self.head = None
        self.temp = None
    def Printing(self):
        
        if self.head is None:
            print("The linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data,"--->>>",end="")
                n = n.ref
    def add_begin(self,data):
        Newnode = Node(data)
        Newnode.ref = self.head
        self.head = Newnode 

    def addend(self,data):
        Newnode = Node(data)

        if self.head is None:
            self.head = Newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=Newnode

    def add_after_value(self,data,x):

        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("The list is empty")
        else:
            Newnode = Node(data)
            Newnode.ref = n.ref
            n.ref = Newnode

    def deletenodeatend(self):
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
        while  n is not None:
            n = n.ref
        n.ref = None




lst = []

limit = int(input("Enter the limit"))

for i in range(limit):
    ls = int(input(f"Enter the {i+1} value :-"))
    lst.append(ls)

l = Linked_list()
print("This is the fist status")
l.Printing()

for i in lst:
    l.addend(i)

print("This is the  status after adding some values")
l.Printing()


lst = []
val = int(input("Enter the value to be added a specific value"))
limit = int(input("Enter the limit of elements to add to :-"))

for i in range(limit):
    ls = int(input(f"Enter the {i+1} value :-"))
    lst.append(ls)

for i in lst:
    l.add_after_value(i,val)
print("The data after add some values into a position")
l.Printing()

