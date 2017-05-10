class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def insert(node,data):
    if node is None:
        return Node(data)
    if data>node.key:
        node.right=insert(node.right,data)
    if data<node.key:
        node.left=insert(node.left,data)
    return node

def LCA(root,a,b):
    if root is None:
        return None
    if root.key>a and root.key>b:
        return LCA(root.left,a,b)
    if root.key<a and root.key<b:
        return LCA(root.right,a,b)
    return root


root=None
root=insert(root,20)
insert(root,8)
insert(root,22)
insert(root,4)
insert(root,12)
insert(root,10)
insert(root,14)

a,b=10,14
t=LCA(root,a,b)
if t is not None:
    print("LCA is",t.key)
else:
    print("Element Not Found")
