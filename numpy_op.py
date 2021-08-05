import numpy as np
#基礎運算
#逐元運算
data1 = np.array([1,3,9])
data2 = np.array([2,4,6])
result1 = data1 + data2
print("加法:",result1)
result2 = data1 * data2
print("乘法:",result2)
result3 = data1 > data2
print("大於:",result3)
result4 = data1 == data2
print("是否相等:",result4)
print("---------------------------------------")
#矩陣運算
dataE1 = np.array([[1,3]]) #1*2
dataE2 = np.array([[1,2,3],[4,5,6]]) #2*3
resultI = dataE1.dot(dataE2)  #內積
print(resultI)
resultO = np.outer(dataE1,dataE2) #外積
print(resultO)
print("---------------------------------------")
#統計運算
data = np.array([[2,1,7],[8,4,5]])  #2*3
result = data.sum()
print("總和:",result)
result = data.max()
print("最大:",result)
result = data.mean()
print("平均數:",result)
result = data.std()
print("標準差:",result)
print("============================================")
result = data.sum(axis = 0)  #欄總和 column (第一維度總和)
print("總和:",result)
result = data.sum(axis = 1)  #列總和 row (第二維度總和)
print("總和:",result)
result = data.mean(axis = 1)  #列總和 row (第二維度總和)
print("平均數:",result)
result = data.cumsum()
print("累加:",result)
result = data.cumsum(axis = 0) #欄做逐次累加
print("欄累加:",result)
result = data.cumsum(axis = 1) #列做逐次累加
print("列累加:",result)