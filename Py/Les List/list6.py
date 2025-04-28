l1 = [1,2,3,4,5,6,7,8,9,66,88,99]
l2 = [7,8,9,66,88,99,1,2,45,56,87,78]
l3 = []
l1.sort()
l2.sort()
for i in range(min(len(l1), len(l2))):
    if l1[i] == l2[i]:
        l3.append(l1[i])
print(l3)