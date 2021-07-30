file = open ("data.txt",mode = "w",encoding = "UTF-8") 
file.close()
with open("data.txt",mode = "w",encoding = "UTF-8") as file:
    file.write("Hello File\n world\n我是")
with open("data.txt",mode = "r",encoding = "UTF-8") as file:
    data = file.read()
with open("data.txt",mode = "w",encoding = "UTF-8") as file:
    file.write("7\n6\n5")
sum = 0
with open("data.txt",mode = "r",encoding = "UTF-8") as file:
    for line in file:
        sum += int(line)
print(sum)