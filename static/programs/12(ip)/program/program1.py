import numpy as np
print("origional array:")
arr1=np.arange(10)
print(arr1)
#Display array in reverse order
print("Revese order")   
arr2 = arr1[::-1]
print(arr2)
#Display even order index
print("Even order index")
arr3 = arr1[2:10:2]
print(arr3)
#Display the sum of first half and seconf half separately
print("Elements of first half:")
arr4 = arr1[:5]
print(arr4)
sum = np.sum(arr4)
print("sum of first half of an array:", sum)
print("Elements of second half:")
arr5 = arr1[5:]
print(arr5)
sum = np.sum(arr5)
print("sum of second half of an array:", sum)
