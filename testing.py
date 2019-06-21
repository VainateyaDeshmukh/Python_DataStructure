import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import scipy as sc


data = pd.read_csv("C:\\PyProj\\datafilesforchart\\loan prediction.csv")
type(data)
data.columns
data.shape

data.tail()
data.head()
data.Loan_ID.head()
data['Loan_ID'].head()
data[['Loan_ID','Married']].head()

data.iloc[1,0]
data.iloc[1,:]
data.iloc[:,0]
data.iloc[0:5,:]
data.iloc[:,0:2]
data.iloc[[0,2],[2,5]]
data.iloc[0:3,1:5]

a1 = data.loc[2,'LoanAmount']
a2 = data.loc[2,['LoanAmount']]
aa = data.loc[2.5,['LoanAmount']]
bb = data.loc[2:5,['LoanAmount']]
cc = data.loc[2:5,['LoanAmount','ApplicationIncome']]

df1 = data.set_index("Loan_ID")
data.set_index("Loan_ID",inplace=True)

df = data.loc['LP001005',['LoanAmount','ApplicantIncome']]
df = data.loc[['LP001005','LP001008'],['LoanAmount','ApplicantIncome']]

data.reset_index(inplace=True)

#data.reset_index(inplace=True,drop=True)
df = data[data['Education']=='Graduate']
df = data[data.Education =='Graduate']
df = data[(data.Education == 'Graduate')&(data.Self_Employed == 'Yes')]
df = data[(data.Education == 'Graduate')&(data.ApplicationIncome >= 5000)]
df = data[(data.LoanAmount <= 40)|(data.LoanAmount >= 400)]
df = data[(data.Dependents!='0')]


data['LoanAmount'].sum()
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Null Values
aa = data.isnull()
data.isnull().sum()
data['LoanAmount'].isnull().sum()

df = data[data['LoanAmount'].isnull()]
df = data[(data.LoanAmount.isnull())& (data.Dependents.isnull())]


dfna = data['LoanAmount'].fillna((data['LoanAmount'].mean()))

#Sorting
datasort = data.sort_values('LoanAmount')
data.sort_values('LoanAmount',inplace = True)
data.sort_values('LoanAmount',inplace = True,ascending = False)


data['Dependents'].unique()
len(data['LoanAmount'])

aa = data['Gender'].value_counts()
bb = data['LoanAmount'].value_counts()

data['LoanAmount'].groupby([data['Married']]).describe()
data['LoanAmount'].groupby([data['Married'],data['Education']]).describe()

data['LoanAmount'].groupby([data['Married']]).mean()

#Pivot Table
p1 = pd.pivot_table(data,index = ['Education'])
p2 = pd.pivot_table(data,index = ['Education','Self_Employed'])
p3 = pd.pivot_table(data,index = ['Education'],values = 'LoanAmount')
print(p3)
p4 = pd.pivot_table(data,index = ['Education'],values=['LoanAmount','ApplicantIncome'])
print(p4)


import numpy as np
pd.pivot_table(data,index = ['Education'],values=['LoanAmount','ApplicantIncome'],aggfunc=[np.sum])
#crosstab
pd.crosstab(data.Education,data.Self_Employed)
pd.crosstab(data.Education,data.Self_Employed,margins=True)
pd.crosstab(data.Education,data.Self_Employed,margins=True,normalize= 'index')

#series
arr1 = np.array(['a','b','c','d'])
sr1 = pd.Series(arr1)
sr1

#arr1 = sr1.Values
sr2 = pd.Series(arr1,index=["id1","id2","id3","id4"])
sr2

dict1 = {1:'jan',2:'feb',3:'mar'}
#dict1={10:'jan',20:'feb',30:'mar'}

sr3 = pd.Series(dict1)
sr3
sr3[3]

#data Frame
#from list

list1 = [['s1',10],['s2','50']]
df = pd.DataFrame(list1,columns= ['stock','price'])
df

df.insert(1,'qnt',0)
listq = [20,15]
df['qnt']=listq

dict2 = {"Stock":['s1','s2'],"Price":['100','200']}
df1 = pd.DataFrame(dict2)
df1

dict2 = {'stock':['s11'],'price':[40]}
df2 = pd.concat([df1,df2],ignore_index=True)
df2

df12 = pd.concat([df1,df2])
df12

#df12 = df1.append(df2,ignore_index = True)
df1['qnt'] = pd.series([100,200])
df1

#drop column
df2 = df1.drop('qnt',axis = 1)
df2 = df1.drop(['stock','qnt'],axis = 1)

#drop row
df2 = df1.drop(0,axis=0)
df2
dict2 = {"Stock":['s1','s2'],"Price":['100','200']}
df1 = pd.DataFrame(dict2)
df1

dict2 = {'stock':['s11'],'price':[40]}
df2 = pd.concat([df1,df2],ignore_index=True)
df2

df12 = pd.concat([df1,df2])
df12

#df12 = df1.append(df2,ignore_index = True)
df1['qnt'] = pd.series([100,200])
df1

#drop column
df2 = df1.drop('qnt',axis = 1)
df2 = df1.drop(['stock','qnt'],axis = 1)

#drop row
df2 = df1.drop(0,axis=0)
df2

dict1 = {'stock':['s1',np.nan,'s3'],'price':[np.nan,np.nan,40]}
df1 = pd.DataFrame(dict1)
df1
df2 = df2.dropna()
df2 = df1.dropna(thresh=2)
df2

#Columns NAme
collist=df1.columns.tolist()
collist

df2  = df1.rename(columns={'stock':'stock2','price':'price2'})
df2

data = pd.read_csv("C:\\PyProj\\datafilesforchart\\loan prediction.csv")
data1 = data
data.iloc[1,0]
data1.iloc[1,0]
data1.iloc[1,0]='100'
data.iloc[1,0]
data1.iloc[1,0]

data2 =data.copy()
data2.iloc[1,0] = '100'
data.iloc[1,0]

data1.iloc[1,0]

#memory address

hex(id(data))
hex(id(data1))
hex(id(data2))
hex(id(df))
