import pandas as pd
import numpy as np
list =[10,20,30,40,50,60]
ser = pd.Series(list)   #craeting series in pandas
print(ser)
df=np.percentile(ser,q=[75,100]) #finding percentile 75% and above
print("Element that are above the 75% percentile\n",df)
