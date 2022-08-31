import pandas as pd
import numpy as np
import random
stu_data = {"stu_name":['Anisdh','Kirti','Piyush','Reena','Mayank'],
        "stu_roll":[10,19,23,29,30]}
df = pd.DataFrame(stu_data)
print("Original Data\n",df)
print("---------------------------------------------------------------")
#Adding new column English and taking random numbers for marks
English=random.sample(list(range(40,100)),k=5)
df['English']=English
#Adding new column Maths_marks and taking random numbers for marks
Maths=random.sample(list(range(40,100)),k=5)
df['Maths']=Maths
#Adding new column Science and taking random numbers for marks
Science=random.sample(list(range(40,100)),k=5)
df['Science']=Science
#Adding new column Hindi and taking random numbers for marks
Hindi=random.sample(list(range(40,100)),k=5)
df['Hindi']=Hindi
#Adding new column SST and taking random numbers for marks
SST=random.sample(list(range(40,100)),k=5)
df['SST']=SST
#finding percentage of the the student
sum=df.sum(axis=1, skipna=None, numeric_only=True)
Percentage=sum*100/500
df['Percentage']=Percentage
print("Student data after adding marks of 5 subject(random)and their percentage \n",df)
