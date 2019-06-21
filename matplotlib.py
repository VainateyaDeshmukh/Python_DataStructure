import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import os
os.chdir("C:\Akash Patil\python data")

dfCol = pd.read_csv("Column.csv")
dfPie = pd.read_csv("Pie.csv")
dfLine = pd.read_csv("Line.csv")
dfScatter = pd.read_csv("Scatter.csv")
data = pd.read_csv("loan prediction.csv")


lst1 = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,2017]
lst2 = [5,6,7,6,7,9,9,10,10,11]

plt.xlabel('Year')
plt.ylabel('Inflation')
plt.title('Trend of Inflation')
plt.plot(lst1,lst2)
plt.plot(lst1,lst2,marker = '+')
dfLine.plot.line('Year','Inflation')

plt.plot(dfLine['Year'],dfLine['Inflation'])
plt.plot(dfLine['Year'],dfLine['Premium'])
plt.title('Premium vs Inflation')
plt.xlabel('Year')
plt.ylabel('percentage')
plt.legend()

dfCol.plot.bar('Months','Yr-2016')
dfCol.plot('Months','Yr-2016',kind = 'bar')
dfCol.plot.bar('Months','Yr-2016',color = "green", legend = True)
dfCol.plot.bar('Months',['Yr-2016','Yr-2017'])

dfPie.plot.pie('Sales',labels =dfPie['Category'],legend = False, autopct = '%.lf%%')

dept = ['Research','Accounts','HR','IT']
emp = [500,100,200,800]
plt.pie(emp,labels = dept, autopct = '%.lf%%')

data['LoanAmount'].groupby([data['Married']]).describe()
data.boxplot(column = 'LoanAmount',by = 'Married')
data.boxplot(column = 'LoanAmount',by = 'Married',figsize = [10,8])
data['LoanAmount'].plot.hist(bins = 200)

dfScatter.plot.scatter('Income','Insurance')
plt.scatter(dfScatter['Income'],dfScatter['Insurance'],color = 'green')
plt.title('Insurance Estimate')
plt.xlabel('Income')
plt.ylabel('Insurance')
plt.savefig('Figure 1.pdf')

df1 = data['LoanAmount'].groupby([data['Married']]).mean()
df1.plot.bar()

df1 = data['LoanAmount'].groupby([data['Dependents']]).sum()
df1.plot.pie(autopct = '%.lf%%')

fig,axs = plt.subplots(2,2)
dfCol.plot.bar('Months','Yr-2016',color = 'green', legend = False, ax = axs[0,0])
data['LoanAmount'].plot.hist(bins = 50, ax = axs[0,1])
dfLine.plot.line('Year','Inflation',ax = axs[1,0])
dfScatter.plot.scatter('Income','Insurance',ax = axs[1,1])
plt.suptitle('Categorical Plotting')
plt.savefig('multichart1.pdf')