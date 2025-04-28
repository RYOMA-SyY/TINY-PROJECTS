list = [9,6 ,7, 6, 5, 4, 3, 2, 1]
print("b4 delte : ", list)
supp = int(input("Enter le numero que tu veux supprimer : "))
if supp in list:
    index = list.index(supp)
    list.pop(index)
else:
    print(f"{supp} is not in the list")
print(list)