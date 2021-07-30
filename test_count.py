a = input("請輸入:")
b = int(a)
if b == 5:
    print("是5")
elif b < 0:
    print("太小")
else:
    print("OK")

#四則運算
n1 = int(input("輸入數字1:"))
n2 = int(input("輸入數字2:"))
op = input("運算方法:+, - , * ,/")
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("輸入錯誤!!")