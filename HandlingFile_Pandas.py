import pandas as pd
data = pd.read_csv('loan prediction.csv')

a1 = data.loc[2,'LoanAmount']
a2 = data.loc[2,['LoanAmount']]
aa = data.loc[2:5,'LoanAmount']
bb = data.loc[2:5,['LoanAmount']]
cc = data.loc[2:5,['LoanAmount','ApplicantIncome']]

df1 = data.set_index("Loan_ID")

data.set_index("Loan_ID", inplace = True)

df = data.loc['LP001005',['LoanAmount','ApplicantIncome']]
df = data.loc[['LP001005','LP001008'],['LoanAmount','ApplicantIncome']]

data.reset_index(inplace = True)

#df = data[data['Education']== 'Graduate']
df = data[(data.Education == 'Graduate') & (data.Self_Employed == 'Yes')]

df = data[(data.Education == 'Graduate') & (data.ApplicantIncome >= 5000)]

df = data[(data.LoanAmount <= 40) | (data.LoanAmount>= 400)]

df = data[data.Dependents != '0']

data['LoanAmount'].sum()

data['TotalIncome'] = data['ApplicantIncome'] +\
                      data['CoapplicantIncome']

aa = data.isnull()

data.isnull().sum()
data['LoanAmount'].isnull().sum()

dfn = data[data.LoanAmount.isnull()]
dfn = data[data['LoanAmount'].isnull()]
#dfn = data[(data.LoanAmount.isnull()) & (data.Dependents.isnull())]

dfn1 = data.LoanAmount.fillna(0)
dfna2 = data.LoanAmount.fillna((data.LoanAmount.mean()))

datasort = data.sort_values('LoanAmount')
data.sort_values('LoanAmount',inplace = True)
a = data
data.sort_values('LoanAmount',inplace = True, ascending = False)

data['Dependents'].unique()
len(data.LoanAmount)

aa = data['Gender'].value_counts()
bb = data['LoanAmount'].value_counts()

#group
aa = data.LoanAmount.groupby([data.Married]).describe()
data.LoanAmount.groupby([data.Married,data.Education]).describe()
data.LoanAmount.groupby([data.Married,data.Education]).mean()
aa = data.LoanAmount.groupby([data.Married,data.Education]).mean()
dft = data['LoanAmount'].groupby([data['Married'],data['Education']]).describe()

#pivot

p1 = pd.pivot_table(data,index = ['Education'])

p2 = pd.pivot_table(data,index = ['Self_Employed','Education'])

p3 = pd.pivot_table(data, index = ['Education'], values='LoanAmount')

p4 = pd.pivot_table(data, index = ['Education'], values = ['LoanAmount','ApplicantIncome'])

import numpy as np
pd.pivot_table(data, index = ['Education'], values = ['LoanAmount','ApplicantIncome'],aggfunc = [np.sum])
pd.pivot_table(data, index = ['Education'], values = ['LoanAmount','ApplicantIncome'],aggfunc = [np.sum,np.mean])
pd.pivot_table(data, index = ['Education'], values = ['LoanAmount','ApplicantIncome'],columns = ['Self_Employed'],aggfunc = [np.sum,np.mean])

