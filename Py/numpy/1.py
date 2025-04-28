import numpy as np
import random 

arr = np.arange(10)
print(arr)

bar = arr * 2
print(bar.ndim)

nar = np.array([[1,2] , [3,4] , [5,6]])

print(nar.ndim) # .ndim returtns the number of dimensions of the array 
print(nar.shape)# .shape returns the how much there's rows and coloms of the array
print(nar.size) # .size returns the total number of elements in the array

bar.reshape(20)



