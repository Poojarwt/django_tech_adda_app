import numpy as np
#creatind 2D array
arr1 = np.arange(16).reshape(4,4)
print("A 2D Array \n", arr1)
print("The Sum of Rows of the array is:")
#Finding the sum of rows in the array
sum_row = np.sum(arr1, axis=0)
print (sum_row)
#Finding the sum of columns in the array
print("The Sum of columns of the array is:")
sum_column = np.sum(arr1, axis=1)
print (sum_column)
#Finding the sum of diagonal in the array
print("The Sum of rows of the array is:")
diag_element = np.diag(arr1)
sum_diag=np.sum(diag_element)
print(sum_diag)
#Slicing the array to get the desired output
print("New array for slicing")
arr2=np.array([[10,20,30,40],[11,21,31,41],[12,22,32,42],[13,23,33,43]])
print (arr2)
print ("After slicing the desired output")
Sl= arr2[2:,1:3]
print(Sl)
