import pandas as pd
#Addition of Rows
df1=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df1=df1.append(df2)
print("Addition of rows in the dataframe:\n",df1)
#Deletion of Rows
df1=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df1=df1.append(df2)
df1=df1.drop(0)
print("Deletion of rows in the dataframe with label 0:\n",df1)
