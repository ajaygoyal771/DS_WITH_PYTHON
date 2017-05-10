class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def insert(root,data):
    new_node=Node(data)
    if root is None:
        return new_node
    elif root.data > data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root

def findpresuc(root,key):
    if root is None:
        return
    if root.data==key:
        if root.left is not None:
            temp=root.left
            while temp.right is not None:
                temp=temp.right
            findpresuc.pre=temp
        if root.right is not None:
            temp=root.right
            while temp.left is not None:
                temp=temp.left
            findpresuc.suc=temp
        return
    if root.data > key:
        findpresuc.suc=root
        findpresuc(root.left,key)
    else:
        findpresuc.pre=root
        findpresuc(root.right,key)



root=None
root=insert(root,50)
insert(root,30)
insert(root,20)
insert(root,40)
insert(root,70)
insert(root,60)
insert(root,80)
findpresuc.pre=None
findpresuc.suc=None
findpresuc(root,65)
if findpresuc.pre is not None:
    print("Predecessor is=", findpresuc.pre.data)
else:
    print("No Predecessor")

if findpresuc.suc is not None:
    print("Successor is=", findpresuc.suc.data)
else:
    print("No Successor")
