#Iterable資料型態
#可疊代資料
    #字串(string)
    #列表(List)
    #集合(SET)
    #字典(Dictionary)
#for
data1 = ([3,4,5])
for x in data1:
    print(x)
data2 = ("abc")
for x in data2:
    print(x)
data3 = {"hello",3.14,78,"A"}
for x in data3:
    print(x)
data4 = {"a":1,"b":2,"c":3}
for x in data4:
    print(x)
    print(data4[x])
#內建函式
    #max(可疊代資料)
    #sorted(可疊代資料)
#max
result1 = max([10,8,1,3])
print(result1)
result2 = max("xyz")
print(result2)
result3 = max([10,15,8,1])
print(result3)
result4 = max({"x":3,"b":7})
print(result4)
#sorted
result = sorted("cba")
print(result)
result = sorted({10,2,100,1})
print(result)