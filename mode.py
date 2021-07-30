import sys
sys.path.append("modules") #在模組的搜尋路徑列表新增路徑
import geometry
# #print(sys.platform)
# #print(sys.maxsize)
result1 = geometry.distance(1,1,5,5)
print(result1)
result2 = geometry.slope(1,2,5,6)
print(result2)

#調整搜尋模組路徑
#print(sys.path) #印出模組的搜尋路徑