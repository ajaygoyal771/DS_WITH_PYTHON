# Python program for implementation of HeapSort
def heapify(arr,a,b):
    largest=b
    l=2*b+1
    r=2*b+2
    if l < a and arr[l]>arr[b]:
        largest=l
    if r < a and arr[r]>arr[largest]:
        largest=r
    if largest != b:
        arr[b], arr[largest] = arr[largest], arr[b]
        heapify(arr,a,largest)

def heapsort(arr):
    a=len(arr)
    for i in range(a,-1,-1):
        heapify(arr,a,i)
    for i in range(a-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i]),

heapsort(arr)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i]),
