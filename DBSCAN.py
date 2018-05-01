import numpy as np


class DBSCAN:
    def __init__(self, eps = 0.1, minPts = 3):
        self.eps = eps
        self.minPts = minPts
        self.clusterCount = 0

    def fit(self, data):
        # data is a numpy array
        point_count = len(data)
        for i in np.arange(point_count):
            print(data[i])



dbs = DBSCAN()
dbs.fit(np.array([1,2,6,7,8]))
