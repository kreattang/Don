import numpy as np
# a = np.array([[1,2],[3,4]])
# print(a.ndim)
# print(a.dtype)
# print(a.reshape((4,1)))

# b = np.arange(1,10,2)
# print(b)


# c = np.linspace(0,1,11)
# print(c)

# # 创建全1矩阵
# d = np.ones((3,2))
# print(d)

# e = np.random.randn(6,4)
# print(e)

# f = np.arange(10)
# print(f)
# print(f[:4])   #半开闭区间，不包含最后一个元素
# print(f[3:7])
# print(f[3:])
# print(f[2:8:2])
# print(f[2::2])
# print(f[::3])
# a = np.arange(0,51,10).reshape(6,1)+np.arange(10)
# print(a)
# # print(a[0,1],a[5,9])
# # print(a[0,0:6])
# # print(a[:3,6:])
# # print(a[2,:])
# # print(a[:,1])
# # print(a[:,::2])
# # print(a[::3,:])
# print(a[::2,::3])
# a = np.random.randint(10,20,6)
# print(a)
# print(a%2)
# print(a[a%2 == 0])

# a = np.arange(6)
# print(a)
# print(a+5)
# b = np.random.randint(1,5,20).reshape(4,5)
# print(b*3)
#
# b = np.random.random_integers(0,1,(5,3))
# c = np.random.random_integers(1,1,(2,3))
# # print(b)
# # print(c)
# # print(b*c)
# print(np.dot(b,c))
#
a = np.array([1,2,3,4])
# b = np.array([2,3,3,5])
# # print(a==b)
# print((a==b).all(),(a==b).any())
# np.cos()
# np.exp()
# np.sqrt()
# a.sum()
# a.mean()
# a.std()
# a.min()
# a.max()
# a.argmax()   #返回最大元素所在的索引
# a.argmin()