#載入 numpy物件
import numpy as np
#根據列表建立 ndarray 物件
ndar = np.array([3,4,-5])
#簡單觀察
print(ndar) #印出資料
print(ndar.size) #印出資料數量

# ndar3_1 = np.array([[[1,2,3,4],[4,5,6,7]],[[7,8,9,10],[10,11,12,13]],[[14,15,16,17],[18,19,20,21]]])
# ndar3_2 = np.empty([2,3,4])
# ndar3_2 = np.zeros([2,3,4])

#一維陣列
data1 = np.array([1,2,3,4])
print(data1)
data1_e = np.empty(4)  #未指定的
print(data1_e)
data1_z = np.zeros(4) #為零
print(data1_z)
data1_o = np.ones(4) #為1
print(data1_o)
data1_ara = np.arange(4) #連續資料
print(data1_ara)
print("--------------------------------------------")
#二維陣列
data2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data2)
data2_e = np.empty([3,3])
print(data2_e)
data2_z = np.zeros([2,3])
print(data2_z)
data2_o = np.ones([3,2])
print(data2_o)
print("--------------------------------------------")
#三維陣列
data3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(data3)
data3_e = np.empty([2,3,4])
print(data3_e)
data3_z = np.zeros([2,3,4])
print(data3_z)
data3_o = np.ones([4,3,2])
print(data3_o)
print("--------------------------------------------")
#高維陣列(4維範例)
data4 = np.array([ [
                        [
                            [1111,1112,1113,1114,1115],[1121,1122,1123,1124,1125],[1131,1132,1133,1134,1135],[1141,1142,1143,1144,1145]
                        ],
                        [
                            [1211,1212,1213,1214,1215],[1221,1222,1223,1124,1225],[1231,1232,1233,1234,1235],[1241,1242,1243,1244,1245]
                        ],
                        [
                            [1311,1312,1313,1314,1315],[1321,1322,1323,1324,1325],[1331,1332,1333,1334,1335],[1341,1342,1343,1344,1345]
                        ]
                    ],
                    [
                        [
                            [2111,2112,2113,2114,2115],[2121,2122,2123,2124,2125],[2131,2132,2133,2134,2135],[2141,2142,2143,2144,2145]
                        ],
                        [
                            [2211,2212,2213,2214,2215],[2221,2222,2223,2224,2225],[2231,2232,2233,2234,2235],[2241,2242,2243,2244,2245]
                        ],
                        [
                            [2311,2312,2313,2314,2315],[2321,2322,2323,2324,2325],[2331,2332,2333,2334,2335],[2341,2342,2343,2344,2345]
                        ]
                    ] 
                ])
print(data4)