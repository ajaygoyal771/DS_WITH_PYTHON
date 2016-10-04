import math
def sear(list2,a,b,c):
    if b >= a:
        mid=(b+1)/2;
        d=int(math.floor(mid));
        if(list2[d] == c):
            return d+1;
        elif(list2[d] < c):
            return sear(list2,d+1,b,c);
        else:
            return sear(list2,a,d-1,c);
    else:
        return -1;
print("Enter the number of values in list\n");
t=int(input())
list1=[];
for i in range(t):
    x=int(input());
    list1.append(x);
print("Enter the element to be searched\n");
y=int(input());
list1.sort();
print(list1);
result = sear(list1,0,t-1,y);
if result == -1:
    print("The element is not found in the list.\n");
else:
    print("The element is found in the list and is at position %d",result);


