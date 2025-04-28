def compter(arr):
    dics = {}
    for char in arr:
        if char in dics:
            dics[char] += 1
        else:
            dics[char] = 1
    return dics




def compter2(arr):
    dics = {}
    exclus =".,;!?"
    for char in arr:
        if char not in exclus:
            if char in dics:
                dics[char] += 1
            else:
                dics[char] = 1

        
    return dics

def nombre_animaux(ferme):
    total = 0
    for nombre in ferme.values():  
        total += nombre  
    return total

def nombre_animal(ferme, animal):
    return ferme.get(animal, 0)


ferme_gaston = {'lapin': 5, 'vache': 7, 'cochon': 2, 'cheval': 4}
print(nombre_animaux(ferme_gaston)) 



string = "helllo"
string2 = "Hello , Whats'S "
print(compter(string))
print(compter2(string2))

