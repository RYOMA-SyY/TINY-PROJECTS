products ={
    "saber" : 229,
    "shuriken" : 29.95,
    "cape" : 75,
    "baguette": 35,
    "chapeau": 12,
    "bandeau": 12,
    "balai": 130,
}
def Dispo(prod,Dict): # (produit , dictionnaire (products))
    if prod in Dict:
        return True
    else:
        return False
    
# print(Dispo("balai",products))



# def sume(dict):
#     moyen = 0
#     for produit in dict :
#         moyen += dict[produit]
#     return moyen
# print(sume(products))

# def sort(m, M, dict):
#     for product, price in dict.items():
#         if m < price < M:
#             print(f"produit {product} : {price} £")
# sort(30,100,products)

panier = {
    "saber": 2,
    "shuriken": 3,
    "bandeau": 1,
}
# def inter(m,M,D):
#     return [x for x in D.keys() if m < D[x] < M ]

# def tousDispo(D1, D2):
#     for key in D1.keys():
#         if not Dispo(key, D2):
#             return False
#     return True

# print(tousDispo(panier,products))

def totale(D1,D2):
    totale =0
    for key,value in D1.items() :
        totale += value * D2[key]
    return totale
print(totale(panier,products))