n = 1
n1 = 1
while n < 5:
    print("變數n是:",n)
    n += 1
for x in [4,1,2]:
    print("列表x是:",x)
for C in "HELLO":
    print("字串是:",C)
for y1 in range(3):
    print("範圍1是:",y1)
for y2 in range(3,6):
    print("範圍2是:",y2)
sum1 = 0
while n1 <= 10:
    sum1 += n1
    n1 += 1
print("while總數:",sum1)

sum2 = 0
for i in range(1,11):
    sum2 += i
print("for總數:",sum2)

n2 = 0
while n2 < 5:
    if n2 == 3:
        break
    print(n2)
    n2 += 1
print("最後n:",n2)

n3 = 0
for i in range(4):
    if i%2 == 0:
        continue
    print(i)
    n3 += 1
print("最後n:",n3)

sum3 = 0
for j in range(11):
    sum3 += j
else:
    print("最後n:",sum3)

#找出平方根
#輸入9 輸出3
#輸入11 輸出沒有
n = input("輸入一個正整數:")
n = int(n) #轉換輸入正整數
for i in range(1,n):
    if i*i == n:
        print("整數平方根:",i)
        break
    else:
        print("沒有整數平方根")