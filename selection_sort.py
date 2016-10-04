def selection_sort(list1,list2,t):
	for i in range(t):
		x=min(list1);
		list2.append(x)
		list1.remove(x)
	return list2
	pass
print("Enter the number of values in list\n");
t=int(input())
list1=[];
for i in range(t):
    x=int(input());
    list1.append(x)
list2=[];
selection_sort(list1,list2,t)
print(list2)
