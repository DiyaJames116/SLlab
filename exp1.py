l=[]
n=int(input("Enter number of elements"))
print("Enter elements in the list")
for i in range (0,n):
    ele=int(input())
    l.append(ele)
print(l)

print("Max element in the list is",max(l))
print("Min element in the list is",min(l))

new_element=int(input("Enter new element to insert into the list"))
l.insert(0,new_element)
print(l)
print("New element inserted at first position")

del_element=int(input("Enter element to be deleted"))
if del_element in l:
    l.remove(del_element)
    print(l)
else:
    print(f"{del_element} not in list")

search_element=int(input("Enter the element to be searched"))
if search_element in l:
    print(f"{search_element} present at index {l.index(search_element)}")
else:
    print(f"{search_element} not present in list")