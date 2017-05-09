class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_List:

    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("\n")

def make_link(a,b):
    newnode=a.head.next
    b.head.next=newnode

def getintersectionnode(a,b):
    x=getcount(a)
    y=getcount(b)
    if(x>y):
        d=x-y
        return _getintersectionnode(d,a,b)
    else:
        d=y-x
        return _getintersectionnode(d,b,a)


def _getintersectionnode(d,a,b):
    new_node1=a.head
    new_node2=b.head

    for i in range(d):
        if(new_node1 is None):
            return -1
        new_node1=new_node1.next

    while new_node1 is not None and new_node2 is not None:
        if new_node1==new_node2:
            return new_node1.data
        new_node1=new_node1.next
        new_node2=new_node2.next
    return -1;

def getcount(a):
    newnode=a.head
    x=0
    while newnode is not None:
        x=x+1
        newnode=newnode.next
    return x


llist=Linked_List()
llist.push(1)
llist1=Linked_List()
llist1.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
make_link(llist,llist1)
llist1.printlist()
llist.printlist()
print("\n")
print(getintersectionnode(llist,llist1))
