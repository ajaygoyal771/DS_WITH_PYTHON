class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,node):
    if root is None:
        root=node
    else:
        if node.val>root.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=' ')
        inorder(root.right)
def search(root,value):
    if root is None:
        print("The value is not present in the tree.")
        return
    elif root.val==value:
        print("The value is present in the tree.")
        return
    elif root.val>value:
        search(root.left,value)
        return
    elif root.val < value:
        search(root.right, value)
        return
r=node(50)
insert(r,node(30))
insert(r,node(20))
insert(r,node(40))
insert(r,node(70))
insert(r,node(60))
insert(r,node(80))
inorder(r)
print("\n")
search(r,90)
