import pandas as pd
import numpy as np
data = pd.read_csv('loan prediction.csv')

#15Nov
pd.crosstab(data.Education,data.Self_Employed)
pd.crosstab(data.Education,data.Self_Employed,margins = True)
pd.crosstab(data.Education,data.Self_Employed,margins = True, normalize='index')

#series

arr1 = np.array(['a','b','c','d'])
sr1 = pd.Series(arr1)
sr1

sr2 = pd.Series(arr1, index = ['id1','id2','id3','id4'])
sr2

sr2.id3

dict1 = {1:'jan' ,2:'feb',3:'mar'}
sr3 = pd.Series(dict1)
sr3[2]

#dataframe
lst1 = [['s1',10],['s2',50]]
df = pd.DataFrame(lst1,columns = ['stock','price'])
df

df.insert(1,'qnt',0)
lstq = [20,15]
df['qnt'] = lstq
df.set_index('stock',inplace = True)

dict2 = {'s1':'10'}
sr0 = pd.Series(dict2)
df3 = pd.DataFrame(sr0)
df3

dict = {'stock':['s1','s2'],'price':[100,200]}
df = pd.DataFrame(dict)
df

dict2={'stock':['s3'],'price':[300]}
df4=pd.DataFrame(dict2)
df4

df34=pd.concat([df,df4],ignore_index=True)
df34

df['qnt']=pd.Series([100,200])
df



#drop coloumn
df4=df.drop('qnt',axis=1)
df4
df4=df.drop(['stock','qnt'],axis=1)       #inplace=True
df4


#del df1[qnt]

#drop row
df5=df.drop(0,axis=0)
df5


dict1 = {'stock':['s1',np.nan,'s3'],'price':[np.nan,np.nan,40]}
dict1 = {'stock':['s1',np.nan,'s3'],'price':[np.nan,np.nan,40]}
df1 = pd.DataFrame(dict1)

df1

df2 = df1.dropna()
df2 = df1.dropna(thresh = 1)  #Keep only the rows with atleast 2 non-na values
df2

#column name
collst = df1.columns.tolist()
collst

df2 = df1.rename(columns={'stock':'stock2','price':'price2'})
df2

#for knowledge

data1 = data
data.iloc[1,0]
data1.iloc[1,0]

data1.iloc[1,0] = '100'
data.iloc[1,0]
data1.iloc[1,0]

data2 = data.copy()
data2.iloc[1,0] = '200'
data.iloc[1,0]
data2.iloc[1,0]
data1.iloc[1,0]

hex(id(data))
hex(id(data1))
hex(id(data2))
hex(id(df))