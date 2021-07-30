#隨機模組
import random
random.random() #固定在0~1取隨機浮點數
random.uniform(0.0,1.0) #指定 (a,b) 間取隨機浮點數
random.randint(0,4) #指定 (a,b) 間取隨機整數
data1 = random.choice([1,5,6,10,20])
print(data1)
data2 = random.sample([1,5,6,10,20],3)
print(data2)
print("--------------------------------------------")
#隨機調換順序
data3 = [1,5,8,20]
random.shuffle(data3)
print(data3)
#隨機亂數
data4 = random.random()
print(data4)
data5 = random.uniform(0.0,1.0) #0.0 到 1.0 之間取隨機福點數
print(data5)

print("--------------------------------------------")
#常態分配亂數
random.normalvariate(100,10) #(平均數,標準差)
data6 = random.normalvariate(100,10) #大約68%
print(data6)
data7 = random.normalvariate(100,20) #大約95%
print(data7)
data8 = random.normalvariate(100,30) #大約99%
print(data8)
print("--------------------------------------------")
#統計模組
import statistics as stat
#計算列表標準差
data9 = stat.mean([1,4,5,8])
print(data9)
data10_1 = stat.mean([1,2,3,4,5,8,100])
data10_2 = stat.median([1,2,3,4,5,8,100])
print(data10_1)
print(data10_2)

data11 = stat.stdev([1,2,3,4,5,8,10])
print(data11)
