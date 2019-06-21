import numpy as np

arr1 = np.array([1,2,3])
print(arr1)
arr1.ndim
arr1.size
arr1.shape
arr1.dtype
np.sum(arr1)
arr10 = np.array(['a','b','c'])
arr10.dtype
arr10 = np.array(['cc',4,5])
arr10.dtype
a4 = np.sqrt(arr1)
a4 = a4.round(2)
arr1*2

# 2 dim array

arr2 = np.array([[1,2,3],[4,5,6]])
arr2.ndim
arr2.size
arr2.shape
a1=np.sum(arr2)
a1
a2=np.sum(arr2,axis = 0)
a2
arr3 = arr2.reshape(3,2)
arr3

arr1 = np.array([1,2,3,4,5])
arr1[1]
arr1[1:3]
arr1[1:]
arr1[:4]

arr1 = np.append(arr1,[6,7])
arr1[2] = 4

arr = np.array([1,2,3,4,5])
arr = np.delete(arr,2)
arr = np.delete(arr,[0,2])

arr11 = np.array([1,5,6])
arr22 = np.array([4,5,6])
arr11+arr22
np.add(arr11,arr22)

arr11.mean()

np.random.seed(1)
arr4 = np.random.randint(low = 1, high = 100, size = 4)
print(arr4)

a1 = np.arange(4,11,2)   #start,stop,step
a1
b1 = a1[2]
b1

a2 = np.linspace(1,15,5)
a2
az = np.zeros((3,7))
az
az.fill(5)
az
az1 = az.ravel()
az1
az1.shape

md1 = np.arange(12).reshape(3,4)
md1
md2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
md2
md2[0,0]
md2[1:]
md2[1:,1:]
md2[1:,[0,2]]