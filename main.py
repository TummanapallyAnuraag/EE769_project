import pandas as pd
from DBSCAN import *
from sklearn.preprocessing import MinMaxScaler
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# dbs = DBSCAN(2**0.5, 1)
# label = dbs.cluster(np.array([ [0,0], [5,5], [11,11], [11, 10], [1,1], [1,0], [10, 10], [100,100] , [2,3]]))
# print(label)

# Using Gas Emissions Data of all States
db = pd.read_csv('data/GasEmissions.csv');
data = np.array(db);
data = data[:,1:]
scaling = MinMaxScaler(feature_range=(0, 1)).fit(data)
data = scaling.transform(data)

dbs = DBSCAN(0.5, 5)
label = dbs.cluster(data)
data_labelled = np.zeros((28,4))
data_labelled[:,:-1] = data
data_labelled[:,-1] = label
print(data_labelled)
label = label + 1*(label == -1)
color = [str(item/255.) for item in label]
print(color)
# plt.scatter(data[:,0], data[:,2], c=color)
# plt.axis('equal')
# plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,0], data[:,1], data[:,2],s=60, depthshade=False, c=color)
plt.show()
