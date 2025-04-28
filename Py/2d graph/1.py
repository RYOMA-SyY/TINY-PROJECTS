import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation



# a1 = [0, 1, 2]
# b1 = [1, 0, 2]

# a2 = [0, 1, 2]
# b2 = [2, 1, 0]

# a3 = [0, 1, 2]
# b3 = [0, 2, 1]





# plt.plot(a2, b2,a1,b1,a3,b3)
# plt.show()
# plt.close()

# x = np.linspace(0,1,21)
# y = x * x
# plt.plot(x,y)
# plt.show()

# a = np.linspace(0,1,21)
# b = np.exp(a)
# plt.plot(a,b)
# plt.show()




# a = np.linspace(0,2*np.pi,101)
# b = np.sin(2*a)
# c = np.sin(3*a)
# plt.plot(c,b)
# plt.show()




# b = np.sin(2*a)
# c = np.sin(3*a)
# plt.plot(a,np.sin(a),'b-.x'    , color="red")
# plt.plot(a,np.sin(a*2),'b-.^'    , color="yellow")
# plt.plot(a,np.sin(a*3),'b-.o'    , color="green")

# plt.subplot(2,2,1)
# a = np.linspace(0,2*np.pi,101)
# plt.title("sinus1")
# plt.xlabel("X")
# plt.ylabel("sin(x)")
# plt.plot(a,np.sin(a),'b-.x', color="red")






# plt.subplot(2,2,2)
# a = np.linspace(0,2*np.pi,101)
# plt.title("sinus2")
# plt.xlabel("X")
# plt.ylabel("sin(x*2)")
# plt.plot(a,np.sin(a*2),'b-.x', color="yellow")








# plt.subplot(2,2,3)
# a = np.linspace(0,2*np.pi,101)
# plt.title("sinus3")
# plt.xlabel("X")
# plt.ylabel("sin(x*3)")
# plt.plot(a,np.sin(a*3),'b-.x', color="green")









# plt.subplot(2,2,4)
a = np.linspace(0,2*np.pi,101)
plt.title("sinus3")
plt.xlabel("X")
plt.ylabel("sin(x*4)")
plt.plot(a,np.sin(a*4),'b-.x', color="blue")


plt.show()

