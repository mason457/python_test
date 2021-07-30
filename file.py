import json
#從檔案讀取JSON資料 放入變數data
with open("config.json",mode = "r") as file:
    data = json.load(file)
    #print("name",data["name"])
    #print("version",data["version"])
print(data)
#data是字典資料
data["name"] = "New Name"  #修改
data["version"] = "1.2.7"  #修改
#新資料寫入
with open("config.json" ,mode="w") as file:
    json.dump(data,file)
