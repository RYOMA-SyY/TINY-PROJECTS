list = [12, 8, 7, 6, 15, 4, 3, 0, 1]
print("b4 sort : ", list)
list.sort()
# print("after sort " ,list)
# n = int(input("Combien de fois du veux ajouter un element : "))
# for i in range(n):
#     list.append(int(input("Enter le numero que tu veux ajouter : ")))

# list.sort()
# print(list)
n = int(input("etrer un element a inserer : "))

for j in range(len(list)):

    if list[j] > n:
        list.insert(j, n)
        break
if j < len(list):
    list.append(n)
   
   
print("Liste après ajout avec tri : ", list)