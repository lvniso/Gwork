import pandas as pd
file = pd.read_csv('data.csv',header=None)
data = file.values
print(data[:,:-1])
print(data[:,-1])