import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import scipy as sc

#assignment no.1 (Question A) TM1817154
# Company can spend maximum 70,000 on training. Training will be approved for each employee in the same order as mentioned in Nomination1dictionary below.
# Following
# data is given:
# Fees
# for each course is:
#     Fee = {'Python': 15000, 'R': 12000}
# Dictionary of employee id and the course they are opting for is:
#
# Nomination1 = {101: 'Python', 102: 'R', 103: 'Python', 104: 'Python', 105: 'R', 106: 'Python', 107: 'R'}
#
# Based on this data, write a function to store the approved output in the dictionary object.
#
# Expected
# output is:
# {101: 'Yes', 102: 'Yes', 103: 'Yes', 104: 'Yes', 105: 'Yes'}
# Note: Solve this using for loop only

def course1(total,fee,nomination1):
    output={}
    try:
        for key in nomination1 :   #alternative -----for key,course in nomination1.items():
            if nomination1[key] in fee:
                total=total - fee[nomination1[key]]
                if total >=0:
                    output[key]='Yes'
                else:
                    total = total + fee[nomination1[key]]
    except Exception as e:
        print("something has gone wrong in: %s-%s" %(key,e))
    print(total)

    return output

total = 70000
fee = {'Python':15000,'R':12000}
nomination1 ={101:'Python',102:'R',103:'Python',104:'Python',105:'R',106:'Python',107:'R'}
print(course1(total,fee,nomination1))

#assignment no.1 (Question B) TM1817154

#Company has a budget of 80,000 for training, cannot exceed this. Training cost for each employee is given below in the dictionary where key is employee id and value is training cost. Approval will be in the sequence of employee id.
# Cost = {101:18000,102:15000,103:18000,104:12000,105:15000,106:15000,107:12000}
#
# Based on this data, write a function to store the approved output in the dictionary object.
# Expected output is:
# {101: 'Yes', 102: 'Yes', 103: 'Yes', 104: 'Yes', 105: 'Yes', 106: 'No', 107: 'No'}
# Note: Solve this using while loop only

def course2(total,cost):
    output = cost
    i=0
    list2 = list(output.keys())
    list1 = list(output.values())
    while i <= len(output) - 1:
        try:
            if total >= list1[i]:
                total = total - list1[i]
                output[list2[i]] = 'Yes'
                i += 1
            else:
                output[list2[i]] = 'No'
                i += 1
        except:
            print("something has gone wrong in:", list2[i])
            i += 1

    return output

total = 80000
cost ={101:18000,102:'gh',103:18000,104:12000,105:15000,106:15000,107:12000}
print(course2(total,cost))


#Assignment2 (Question1)-----------------------------------------------------------------------------------------------------
# Question A:
# List of product and list of corresponding quantity of each product are given below.
# prod = ['Prod1', 'Prod2', 'Prod2','Prod3','Prod1']
# qnt = [10,25,15,20,40]
# Write a function to store total of each product quantity. In the function, you will pass the parameters prod & qnt given above.
# Expected output:{'Prod1': 50, 'Prod2': 40, 'Prod3': 20}
# Note: While writing this code you will need unique value of prod, to get it, use set(prod) command

# TM1817154

def prod_qnt(prod, qnt):
    output = {}
    for i in range(0, len(prod)):
        if prod[i] not in output:
            output[prod[i]] = qnt[i]
        else:
            output[prod[i]] += qnt[i]
    return output


prod = ['Prod1', 'Prod2', 'Prod2', 'Prod3', 'Prod1']
qnt = [10, 25, 15, 20, 40]
print(prod_qnt(prod, qnt))

#Assignment2 (Question2)

# Following data is given:
# qnt1=[10,25,15,20,40]
# price1 = [10,8,5,7,4]
# Write a function to create a list of purchase amount (qnt1*price1) of each item.
# Expected output: [100, 200, 75, 140, 160]
# Note: Calculate using map function

def qnt_price(qnt1,price1):
    return list(map(lambda x,y :x*y,qnt1,price1))

qnt1=[10,25,15,20,40]
price1=[10,8,5,7,4]
print(qnt_price(qnt1,price1))

#Assignment 3 (Question A)--------------------------------------------------------------------------------------------------------------
# There are two categories of bank customers â€“ Regular & Gold customers. Bank Name â€˜ABC Bankâ€™, is a static attribute at class level.
# In this scenario, we have following attributes:
# 	Customer ID (custid)
# 	Name (name)
# 	Method Print Statement (PrintState):
# 		You need to display message: â€œCustomer Statement for Custid : 100, Name : Cust1 â€œ
# For Regular customer :
# Daily Withdrawal limit (wlimit) â€“ Set default to 1000 but can be changed on customer request.
# 	Method for checking bank balance & Print it (chkbal):
# 	If last quarter average balance is less than 10000 then return string â€œLow balance charges will be 100â€ else â€œNo chargesâ€. Use this string to print the output, from the instance of the class.
# Last 12 months balance = [10000, 10000, 15000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 40000, 60000]
# For Gold customer will have:
# 	Name of Relationship manager (RM)
# 	Method for checking bank balance & Print it (chkbal):
# If last year average balance is less than 100000 then return string â€œLow balance charges will be 500â€ else â€œNo chargesâ€. Use this string to print the output, from the instance of the class.
# Last 12 months balance = [100000, 100000, 150000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 40000, 60000]
# You need to set following values for the attributes of the instance of the class (object)
# 	Custid =100
# 	Name = â€˜Cust1â€™
# 	RM = â€˜RM1â€™
# Create appropriate classes and demonstrate how you are using inheritance and polymorphism.


class Customer:
    bank ="ABC BANK"
    def __init__(self,custid,custname):
        # object attributes
        self.id = custid
        self.name = custname
    def print_statement(self):
        print("Customer Statement for Custid : {0}, Name : {1}".format(self.id,self.name))

class Regular_cust(Customer):
    def __init__(self,wlimit,list1,custid,custname):
        # object attributes
        super().__init__(custid,custname)
        self.wlimit = 1000
        self.list=list1
    def checkbal(self):
        a=sum(self.list[-3:])
        super().print_statement()
        if a/3 < 10000:
            string = "Low balance charges will be 100"
        else :
            string ="no charges"
        print(string)

class Gold_cust(Customer):
    def __init__(self,rmname,list1,custid,custname):
        # object attributes
        super().__init__(custid,custname)
        self.rmname = rmname
        self.list=list1
    def checkbal(self):
        super().print_statement()
        a=sum(self.list)
        if a/12 < 100000:
            string = "Low balance charges will be 500"
        else:
            string = "no charges"
        print(string)

def checkbalance(CustType):
    CustType.checkbal()


rmname="RM1"
wlimit=2000
custid=100
custname='Cust1'
list1=[10000, 10000, 15000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 40000, 60000]
list2=[100000, 100000, 150000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 40000, 60000]
g1=Gold_cust(rmname,list2,custid,custname)
r1=Regular_cust(wlimit,list1,custid,custname)

checkbalance(g1)


#Assignment No3 (QuestionB) TM1817154
# Write following string to the file â€˜TextAssign3b.txtâ€™
# â€œThere are some phone no. (022)-2367, (020)-5689, 8970 22, (020)-8945, 020-4599. Also, we have some email aa@abc.com, pqr@abc.com, zz@xyz.com, kk.com â€œ
# You need to extract phone starting with the code format (020) only. Also, extract email with a domain abc.com.


import re
txt="There are some phone no. (022)-2367, (020)-5689, 8970 22, (020)-8945, 020-4599. " \
    "Also, we have some email aa@abc.com, pqr@abc.com, zz@xyz.com, kk.com"

d=re.findall('[\w]+@abc.com',txt)
print(d)

e=re.findall(r'\(020\)\d{3}-\d{4}',txt)
print(e)


#Assignment No 4----------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv("C:\\Users\\Swapnil Bhor\\PycharmProjects\\data\\Emp.csv")
data1=data.copy()
#Question1

# What is the education & income of empid =2 & 5.  Extract using both methods (positional and label name based).
a1=data.iloc[[1,4],[2,6]]#positional
a2=data.loc[[1,4],["Education","Income"]]#Label name based

#Question2
#Get the age of emp where education is â€˜UGâ€™ and income is greater than 5000.

df1=data[(data.Education=='UG') & (data.Income >=5000)].loc[:,["Age"]]
# df4=data[(data.Education=='UG') & (data.Income >=5000)]["Age"]

#Question3
# Sort the same dataframe object in the descending order of income.
data.sort_values('Income',inplace=True,ascending=False)

#Question4

# How to get the following output from the given data?
#            	      Age        		    Income
# Gender      	  F      	M      		 F               M
# Dept
# Research  	29.00  	39.67    		4193.0    4777.0
# Sales         	44.33  	36.00        	4451.0  	  3251.0

p1=pd.pivot_table(data,index=['Dept'],values=['Age','Income'],columns=['Gender'],aggfunc=[np.mean])
p1=round(p1,2)
print(p1)

#Question5
# Create a new dataframe object with two records and combine it with the original dataframe.
# 15	Research	UG	F	No	25	3500
# 14	Sales	PG	M	Yes		4500

#using lists
lst1 = [[15,'Research','UG','F','No',25,3500],[14,'Sales','PG','M','Yes',np.nan,4500]]
df1= pd.DataFrame(lst1,columns=['EmpID','Dept','Education','Gender','Married','Age','Income'])
df13=pd.concat([data1,df1],ignore_index=True)
#using dictionary
dict1={'EmpID':[15,14],'Dept':['Research','Sales'],'Education':['UG','PG'],'Gender':['F','M'],'Married':['M','F'],'Age':[25,np.nan],'Income':[3500,4500]}
df2=pd.DataFrame(dict1)
df23=pd.concat([data1,df2],ignore_index=True)

#Question 6

# Create bar chart using following data:
# city = ['Mumbai', 'Pune', 'Chennai', 'Delhi']
# Customers = [1200, 1000, 800, 1500]

city = ['Mumbai', 'Pune', 'Chennai', 'Delhi']
Customers = [1200, 1000, 800, 1500]
plt.bar(city,Customers,width=.5)
plt.xlabel('City')
plt.ylabel('Customers')
plt.title('City vs Customers')
plt.show()

#Question7
# Create Numpy array in the range of 0 to 50 which is multiple of 10.
# Create another array of random number between 100 to 200.  Add both the arrays.
# Make sure that result should not keep changing every time.

a1 = np.arange(0,50,10)
np.random.seed(123)
a2=np.random.randint(1,100,5)
a3=np.add(a1,a2)

