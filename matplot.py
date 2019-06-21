import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
data = pd.read_csv("C:\PyProj\datafilesforchart\\Emp.csv")
data1=data['Income'].groupby([data['Dept']]).sum()
data1.plot.pie(autopct="%.1f%%")
data1=data['Income'].groupby([data['Dept']])
data.boxplot(column='Income',by='Dept')
data['Income'].plot.hist(bins=20)