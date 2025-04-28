matier = int(input("Combien de matier tu veux ajouter : "))
note_ahmed = []
note_khalid = []
print("Etrer les notes de Ahmed : ")
for i in range(matier):
    note_ahmed.append ( float(input(f"Enter la note de la matier {i+1} : ")))
print("Etrer les notes de Khalid : ")
for i in range(matier):
    note_khalid.append ( float(input(f"Enter la note de la matier {i+1} : ")))
print("Les notes de Ahmed : ", note_ahmed)
print("Les notes de Khalid : ", note_khalid)
moyenne_ahmed = sum(note_ahmed) / matier
moyenne_khalid = sum(note_khalid) / matier
print("La moyenne de Ahmed est : ", moyenne_ahmed)
print("La moyenne de Khalid est : ", moyenne_khalid)
if moyenne_ahmed > moyenne_khalid:
    print("Ahmed est le premier")
elif moyenne_ahmed < moyenne_khalid:
    print("Khalid est le premier")
else:
    print("Les deux sont les memes")


    