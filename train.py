import matplotlib.pyplot as plt
import numpy
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import linear_model
file = pd.read_csv('data/data2.csv',header=None)
data = file.values
base = 1
# print(data[:,:-1])
# print(data[:,-1])
data_X = data[:,:-1]
for i in range(len(data_X)):
    if data[i][4] == 'S':
        data_X[i][4] = base
    elif data[i][4] == 'SW':
        data_X[i][4] = 2*base
    elif data[i][4] == 'SE':
        data_X[i][4] = 3*base
# print(data_X)
data_Y = data[:,-1]
X_train, X_test, Y_train, Y_test = train_test_split(data_X, data_Y, test_size=0.2, random_state=0)

model = linear_model.LinearRegression()
model.fit(X_train,Y_train)
print (model.intercept_)    # 训练后模型权重（特征个数无变化）
print (model.coef_)

Y_pre = model.predict(X_test)
# print(Y_pre)
# print(Y_test)
sum_mean=0
for i in range(len(Y_pre)):
    sum_mean+=(Y_pre[i]-Y_test[i])**2
sum_erro=numpy.sqrt(sum_mean/(len(Y_test)))  #这个10是你测试级的数量
# calculate RMSE by hand
print ("RMSE by hand:",sum_erro)    #做ROC曲线
plt.figure()
plt.plot(range(len(Y_pre)),Y_pre,'b',label="predict")
plt.plot(range(len(Y_pre)),Y_test,'r',label="test")
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()