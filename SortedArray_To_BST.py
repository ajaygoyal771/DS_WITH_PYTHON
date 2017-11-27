class Node():
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.left=None
		self.right=None


def sortedArray_to_BST(arr,start,end):
	if start>end:
		return None
	mid = int((start + end)/2)
	root=Node(arr[mid])
	root.left = sortedArray_to_BST(arr,start,mid-1)
	root.right = sortedArray_to_BST(arr,mid+1,end)
	return root


def Preorder(root):
	if root is None:
		return
	print(root.data, end=' ')
	Preorder(root.left)
	Preorder(root.right)


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
root=sortedArray_to_BST(arr,0,n-1)
print("Preorder Traversal of the tree is")
Preorder(root)
