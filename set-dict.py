#集合運算
#s1 = {3,4,5}
#print(3 not in s1)
s1 = {3,4,5}
s2 = {4,5,6,7}
s3 = s1 & s2 #交集
print(s3)
s4 = s1 | s2 #聯集
print(s4)
s5 = s1 - s2 #差集
print(s5)
s6 = s1 ^ s2 #反交集 兩者不交集部分
print(s6)
s = set("hello")
print(s)
print("H" in s)

#字典運算
dic = {"apple":"蘋果","bug":"蟲"}
print(dic["apple"])
print ("apple" in dic)
print(dic)
del dic["apple"]
print(dic)

dic1 ={x:x*2 for x in []}
print(dic1)