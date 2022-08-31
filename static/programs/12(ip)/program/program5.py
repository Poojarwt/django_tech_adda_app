import numpy as np
#creating 2D numpy array
arr1 = np.arange(15).reshape(3,5)
arr2 = np.arange(15,30).reshape(3,5)
print("Element of first array:\n",arr1)
print("Element of Second array:\n",arr2)
print("------------------------------")
#join two arrays column wise
stack_horizontal= np.hstack((arr1,arr2))
print("Array stack together column wise\n",stack_horizontal)
print("------------------------------")
#join two arrays row wise
stack_vertically= np.vstack((arr1,arr2))
print("Array stack together row wise\n",stack_vertically)
print("------------------------------")
#join two arraysusing concatenate
stack= np.concatenate((arr1,arr2))             # join two array row wise
stack1= np.concatenate((arr1,arr2),axis=1)     # join two array column wise
print("Array stack together row wise\n",stack,"\n Array stack together column wise\n",stack1)
print("------------------------------")
