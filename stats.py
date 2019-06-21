import pandas as pd
import numpy as np
from scipy import stats
data = pd.read_csv("C:\\PyProj\\datafilesforchart\\loan prediction.csv")
type(data)
data.columns
data.shape

data.describe()
data['LoanAmount'].describe()
data['LoanAmount'].describe()['mean']
data['LoanAmount'].describe()['count']
data['LoanAmount'].describe()['max']
data['LoanAmount'].describe()['min']
data['LoanAmount'].describe()['25%']
data['LoanAmount'].mean()
data['LoanAmount'].mode()
data['LoanAmount'].std()
data['LoanAmount'].var()
data['LoanAmount'].median()

x = [1,4,5,6,6,2,3]
np.mean(x)
np.median(x)
np.sqrt(x)

#option 1
x_np = np.array(x)
std1 = x_np.std()
print(std1)

#option 2(formula based)
mean1 = sum(x)/len(x)
n = int(len(x))
lst1 = [(val - mean1)**2 for val in x]
std = (sum(lst1)/n)**0.5
print(std)

np.random.seed(10)
arr =  np.random.randint(low=0,high=50,size=40)
print(arr)

#Data Scaling
#Z-Score - (x-mean)/std
z_score = [(val - mean1)/std1 for val in x]
dict1  = dict(zip(x,z_score))
print(dict1)

#z_score = np.round(np.array(z_score),2)
#min-max scaling
minmax = [(val - min(x))/(max(x)- min(x)) for val in x]
dict1 = dict(zip(x,minmax))
print(dict1)

#Using Library (Won't be in exam)
from sklearn.preprocessing import StandardScaler
import scipy.stats as st
data2 = data[['ApplicantIncome','LoanAmount']]
data2.isnull().sum()
#data2.filling(0,inplace=True)
data3 = data2.fillna(0)

#z = (x-mean)/std dev
sc = StandardScaler()
data4 = sc.fit_transform(data3).round(4)
data5 = pd.DataFrame(data4)
data5.columns= ['ApplicantIncome','LoanAmount']

#chisquare - sum(((o-e)**2)/e) **o-observed & e-expected
import scipy.stats as stats
#no of student passed in sub1...sub6
passed = [30,14,34,45,57,20]
exptedNum = [20,20,30,40,60,30]
pass1 = np.array([30,14,34,45,57,20])
exp1 = np.array([20,20,30,40,60,30])
chi_squared_stat =(((pass1-exp1)**2)/exp1).sum()
print(chi_squared_stat)

#hypothesis
chi1 = st.chisquare(f_obs=passed,f_exp=exptedNum)
prob = 0.95
dof = 5
critical = st.chi2.ppf(prob,dof)

#Anova 1
lsta = [3,2,1]
lstb = [5,3,4]
lstc = [5,6,7]
lstAll = lsta+lstb+lstc
meanAll = np.mean(lstAll)
SST = sum([(x - meanAll)**2 for x in lstAll])   #Sum of Square Total
n=8

m1=np.mean(lsta)
m2=np.mean(lstb)
m3=np.mean(lstc)
SSW = sum([(x - m1)**2 for x in lsta])+sum([(x - m2)**2 for x in lstb])+sum([(x - m3)**2 for x in lstc])
nw = 6  #Dof->m8(n-1)

SSB = 3*((meanAll-m1)**2 +(meanAll-m2)**2+(meanAll-m3)**2)
nb = 2 #Dof->m-1

rSSB = (SSB/nb)
rSSW = (SSW/nw)
Statistics.txt
Displaying Statistics.txt.