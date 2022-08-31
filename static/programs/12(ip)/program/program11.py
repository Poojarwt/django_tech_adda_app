import numpy as np
import matplotlib.pyplot as plt
data=[1,11,21,31,41]
plt.hist([5,15,25,35,45],bins=[0,10,20,30,40,50],
       weights=[5,10,30,25,32],edgecolor="red",histtype='step')
plt.xlabel('Number of students')
plt.ylabel('Marks obtained')
plt.title('Frequency polygon')
plt.show()
