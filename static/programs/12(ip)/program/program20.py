import pandas as pd
import numpy as np
data={'Name':['Aman','Bhanu','Charu','Aman','Bhanu','Charu',
              'Aman','Bhanu','Charu','Aman','Bhanu','Charu'],
      'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
              'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
      'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
df=pd.DataFrame(data,columns=['Name','Exam','Subject','Score'])
print(df)
df1=pd.pivot_table(df, index='Exam',columns='Name',values='Score')
print("Data after applying pivot_function\n",df1)
