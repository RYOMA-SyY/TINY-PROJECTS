import numpy as np

# Création d'un tableau 2D
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accès aux éléments :
print(arr[0, 1])    
print(arr[:, 2])    
print(arr[1:3, :])  

# Modification :
arr[1, 1] = 10       



# np.zeros : Remplit de 0
zeros = np.zeros((2, 3))
print(zeros)  

# np.ones : Remplit de 1
ones = np.ones((2, 2)) 
print(ones)   

 






a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# Concaténation verticale (axe 0)
concat_v = np.concatenate((a, b), axis=0)
print(concat_v)      

# Concaténation horizontale (axe 1)
concat_h = np.concatenate((a, b.T), axis=1)
print(concat_h)