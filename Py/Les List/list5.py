list = [9, 8, 7, 6, 5, 4, 3, 2, 1,1,1,1]
print("b4 delete: ", list)
supp = int(input("enter the number u want to delete: "))
for i in range(list.count(supp)):
    list.remove(supp)
print("after delete: ", list)