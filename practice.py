def heapify(arr,currentLargest,lenOfArr):
	largest = currentLargest
	l = 2*currentLargest + 1
	r = 2*currentLargest + 2

	if l < lenOfArr and arr[l] > arr[largest]:
		largest = l
	if r < lenOfArr and arr[r] > arr[largest]:
		largest = r
	if largest != currentLargest:
		arr[currentLargest], arr[largest] = arr[largest], arr[currentLargest]
		heapify(arr,largest,lenOfArr) 

def heapsort(arr):
	a = len(arr)
	for i in range(a,-1,-1):
		heapify(arr,i,a)
	for i in range(a-1,-1,-1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr,0,i)



# Driver code to test above
arr = [12, 11, 10, 9, 8, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i]),

heapsort(arr)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i]),