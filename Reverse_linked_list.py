class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

    def push(self,newdata):
        new_node=Node(newdata)
        new_node.next=self.head
        self.head=new_node


    def printlist(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end="->")
            temp=temp.next
        print("\n")
llist=Linkedlist()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print("Given List is\n")
llist.printlist()
print("Reversed Linkedlist is\n")
llist.reverse()
llist.printlist()
