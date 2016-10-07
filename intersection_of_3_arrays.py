def common(list1,list2,list3):
    n1=len(list1)
    n2=len(list2)
    n3=len(list3)
    i=0
    j=0
    k=0
    while i < n1 and j < n2 and k < n3:
        x=list1[i]
        y=list2[j]
        z=list3[k]
        if x==y and y==z:
            print(x)
            i = i + 1
            j = j + 1
            k = k + 1
        elif x < y:
            i = i + 1;
        elif y < z:
            j = j + 1;
        else:
            k = k + 1;

def main():
    list1=[]
    list2=[]
    list3=[]
    print("Enter the total number of elements in first array")
    t=int(input())
    for i in range(t):
        x=int(input())
        list1.append(x)
    print("Enter the total number of elements in second array")
    t = int(input())
    for i in range(t):
        x = int(input())
        list2.append(x)
    print("Enter the total number of elements in third array")
    t = int(input())
    for i in range(t):
        x = int(input())
        list3.append(x)
    common(list1,list2,list3)
main()
