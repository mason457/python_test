import numpy as np
#多維陣列索引 
print("================================================")
#單維度資料
data_s = np.array([1,2,3,4,5])
print(data_s[1])
print("================================================")
#多維度資料
data_t = np.array([[11,12,13],[21,22,23],[31,32,33],[41,42,43]])
print(data_t[0,1]) #12
print(data_t[1,0]) #21
print(data_t[2,0]) #31
print("================================================")
#多維度切片
print(data_t[1:3,0:2])   #[[21,22],[]31,32]
print("------------------------------------------------")
print(data_t[0:2,1])     #[12,22]
print("================================================")
#單維度切片
print(data_s[0:3])   #[1,2,3]
print(data_s[:2])    #[1,2]
print(data_s[2:])    #[3,4,5]
print(data_s[:])     #[1,2,3,4,5]
print("================================================")
#使用 ... (全要)
data_m = np.array([[[111,112,113],[121,122,123],[211,212,213],[221,222,223]]])
print(data_m[0,...])     #[[111,112,113],[121,122,123]]
print("------------------------------------------------")
print(data_m[...,1:3])   #[[112,113],[122,123],[212,213],[222,223]]