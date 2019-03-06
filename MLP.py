from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
file = pd.read_csv('data2.csv',header=None)
data = file.values
base = 1
data_X = [[0 for col in range(5)] for row in range(len(data))]
data_Y = [0 for b in range(len(data))]

for i in range(len(data)):
    data_X[i][0] = data[i][0]
    data_X[i][1] = data[i][1]
    data_X[i][2] = data[i][2]
    data_X[i][3] = data[i][3]
    if data[i][4] == 'S':
        data_X[i][4] = base
    elif data[i][4] == 'SW':
        data_X[i][4] = 2*base
    elif data[i][4] == 'SE':
        data_X[i][4] = 3*base
    data_Y[i] = data[i][5]
# data_Y = data[:,-1]
X_train, X_test, Y_train, Y_test = train_test_split(data_X, data_Y, test_size=0.2, random_state=0)

model = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 5), random_state=1)
model.fit(X_train, Y_train)

res = model.predict(X_test)
print(res)
print(Y_test)