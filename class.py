#定義類別
class IO:
    supportedSrcs = ["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("不支援")
        print("Read from",src)
#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")