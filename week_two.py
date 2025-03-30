#Create an empty list called my_list.
my_list=[]
#Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#Insert the value 15 at the second position in the list.
my_list.insert(1,15)
#Extend my_list with another list: [50, 60, 70].
another_list=[50, 60, 70]
my_list.extend(another_list)
#Remove the last element from my_list.
my_list.remove(70)
print(my_list)
#or
#my_list.pop(7)
#print(my_list)
#Sort my_list in ascending order.
my_list.sort(reverse=True)
print(my_list)
#Sort my_list in ascending order
my_list.sort()
print(my_list)
#Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(index_of_30)