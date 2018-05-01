from DBSCAN import *

dbs = DBSCAN(2**0.5, 1)
label = dbs.cluster(np.array([ [0,0], [5,5], [11,11], [11, 10], [1,1], [1,0], [10, 10], [100,100] , [2,3]]))
print(label)
