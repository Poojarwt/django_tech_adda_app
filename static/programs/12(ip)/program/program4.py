#program to print the Checkerboard pattern
import numpy as np
print("checkerbox pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2]=1
x[::2,1::2]=1
print(x)
