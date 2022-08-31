import pandas as pd
import numpy as np
data = {"item_category":['plastic','plastic','plastic','stationary','stationary','stationary','clothes','clothes','clothes','crockery','crockery','crockery'],
        "item_name":['lunch_box','water_bottle','buckets','pen','notebook','colors','Kurti','t-shirt','jeans','dinner_set','cup_set','spoon_set'],
        "expenditure":[1000,2000,3000,2500,6000,5000,10000,8000,12000,6500,5500,4500]}
df = pd.DataFrame(data)
print("Raw_Data of a shop\n", df)
print("-------------------------------------------")
df1=df.groupby(['item_category','item_name','expenditure'])
print("Data group by category\n", df1.size())
print("-------------------------------------------")
df2=df.groupby(['item_category']).agg([np.sum])
print("Total expenditure per category\n",df2)
print("-------------------------------------------")
#df2=df1.get_group('plastic')
#print(df1)
