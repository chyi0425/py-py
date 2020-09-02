import numpy as np

# 1.从已有数据中创建ndarray
# 将列表转换成ndarry
list1 = [3.14,2.17,0,1,2]
nd1 = np.array(list1)
print(nd1)
print(type(nd1))

# 嵌套列表可以转换成多维ndarray
list2 = [[3.14,2.17,0,1,2],[1,2,3,4,5]]
nd2 = np.array(list2)
print(nd2)
print(type(nd2))

# 2．利用random模块生成ndarray
nd5 = np.random.random([3,3])
print(nd5)
print(type(nd5))

np.random.seed(123)
nd5_1 = np.random.random([2,3])
print(nd5_1)
np.random.shuffle(nd5_1)
print("随机打乱后")
print(nd5_1)

# 3 创建特定形状的多维数组
# 生成全是0的3x3矩阵
nd6 = np.zeros([3,3])
print(nd6)
# 生成全是1的3x3矩阵
nd7 = np.ones([3,3])
print(nd7)
# 生成3阶的单位矩阵
nd8 = np.eye(3)
print(nd8)
# 生成3阶对角矩阵
print(np.diag([1,2,3]))

# 生成的数据保存到磁盘
nd9 = np.random.random([5,5])
np.savetxt(X=nd9,fname='./test2.txt')
nd10 = np.loadtxt('./test2.txt')
print(nd10)

# 利用arange函数 arange([start,] stop[,step,],dtype=Node)

print(np.arange(10))
print(np.arange(0,10))
print(np.arange(1,4,0.5))
print(np.arange(9,-1,-1))

# 1.2 存取元素
np.random.seed(2020)
nd11 = np.random.random([10])
# 获取指定位置的元素，获取第4个元素
nd11[3]
# 截取一段数据
nd11[3:6]
# 截取固定间隔元素
nd11[1:6:2]
# 倒序取数
nd11[::-2]
# 截取一个多维数组的一个区域内数据
nd12 = np.arange(25).reshape([5,5])
nd12[1:3,1:3]
