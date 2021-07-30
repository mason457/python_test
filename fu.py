#定義函式
def multiply(n1,n2):
    value = n1*n2
    print(value)
    return value
#呼叫函式
x = (int)(input("輸入第一個數:"))
y = (int)(input("輸入第二個數:"))
value = multiply(x,y)
print(value)
 
#  #程式的包裝
 

def calculate(max):
     sum = 0
     for n in range(1,max+1):
        sum += n
     print(sum)

calculate(10)
calculate(20)

#參數預設資料
def power(base,exp = 0):
   print(base**exp)
power(3,2)
power(4)

#參數名稱對應
def divide(n1,n2):
   print(n1/n2)
divide(2,4)
divide(n2=4,n1=2)

#不定參數資料

def avg(*numbers):
   sum = 0
   for n in numbers:
      sum += n
   print(sum/len(numbers))

avg(3,4)
avg(3,4,5)
avg(1,4,-1,6)