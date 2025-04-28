# name = {"1":"Ali","2":"Ahmed","3":"Jason","4":"Paul"}
# print(name.get("2"))

# etd1 = {"id":"1","name":"ali","note":12.23}
# etd2 = {"id":"2","name":"paul","note":15.78}
# etd3 = {"id":"3","name":"jason","note":11.3}

# edt =[etd1,etd2,etd3]
# for name in edt :
#     print(name["name"])


#enumerate iteration du deux element par la fois l'indice et la valeur 
# for i , j in enumerate([75,-75,0]):
#     print(i, j)

# notes = {
#     "math":14,
#     "programmation":12,
#     "anglais":16,
#     "biologie":10,
#     "sport":19,
# }
# all = 0
# for matier in notes :
#     all = all + notes.get(matier)
# print(all/len(notes))


# jours = {
#     "lundi":1,
#     "mardi":2,
#     "mercredi":3,
#     "jeudi":4,
#     "vendredi":5,
#     "samedi":6,
#     "dimanche":8,
# }
# jours["dimanche"]=7

# print(jours)

# dict = notes = {
#     "math":14,
#     "programmation":12,
#     "anglais":5,
#     "biologie":10,
#     "sport":19,

# }

# note_accept= {}
# note_decline = {}

# for subject in notes.keys():
#     if notes.values() > 10:
#         note_accept = subject , notes.values()
#     else:
#         note_decline = subject , notes.values()
    

# print(f"note accepter est = {note_accept} \nnote refuser est = {note_decline}")


l1 =[7,12,10,21,5]

peer = {}
for i in l1 :
    if(i % 2 == 0 ) :
        peer = i , "peer"
    else :
        peer = i ,"impeer"
print(peer)





