class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def is_BST(root):
	Min = -4294967296
	Max = 4294967296
	return is_BST_UTIL(root,Min,Max)


def is_BST_UTIL(root,min,max):
	if root is None:
		return True
	if root.data<min or root.data>max:
		return False
	return is_BST_UTIL(root.left,min,root.data-1) and is_BST_UTIL(root.right,root.data+1,max)


root=Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
if is_BST(root):
	print('it is a BST')
else:
	print("it is not a BST")
