import numpy as np
import pandas as pd

class DBSCAN:
    def __init__(self, eps = 0.1, minPts = 3):
        self.eps = eps
        self.minPts = minPts
        self.clusterCount = 0


    def Distance(self, x, y):					#To Calculate Distance between 2 points
        d = np.linalg.norm(x-y)					# To caclulate l2 norm using Linear Algebra Library in numpy
        return d


    def RangeQuery(self, data, i):				# To get the list of Neighbouring points
    	point_count = len(data)					# Total number of points
    	neighbours = np.array([], dtype=int)	# array of indexes of neighbouring points, empty initially
    	for j in np.arange(point_count):
    		d = self.Distance(data[i], data[j])	# calling distance function
    		if d <= self.eps: 					# if point lies within Epsilon boundary then do the following
    			neighbours = np.append(neighbours, [j])	# add to neighbour list
    			# print('Inside RangeQuery:--')
    			# print(neighbours,j)
    	return neighbours


	# ------------------------------------------------
	# Cluster Labelling Rules:
	# ------------------------------------------------
	#  0 	=> Undefined / Unlabelled (Yet to Process)
	# -1 	=> Noise
	#  1	=> Cluster Number 1
	#  2	=> Cluster Number 2
	#  ...
	#  ...
	#  N 	=> Cluster Number N
	# ------------------------------------------------
    def cluster(self, data):						# Function for clustering data
        # data is a numpy array
        point_count = len(data)						# number of data points
        label = np.zeros((point_count), dtype=int)	# Defining Empty Label List


        for i in np.arange(point_count):			# For each point in inuput data do the following
            # print(data[i], label[i])
            if label[i] != 0 :						# if already labelled, skip it
            	# Already the point has a label
            	continue
            # This line is executed when data not labelled yet
            neighbours = self.RangeQuery(data, i)	# Get Epsilon Neighbourhood points of this point (i)
            # print('neighbours of ',i,'th data point are: ')
            # print(neighbours)
            # print('')
            if len(neighbours) < self.minPts:		# If the Number of Neighboring points less than minimum points
            	label[i] = -1						# Label the point i as a Noise, because it is not so densly surrounded
            	# print(neighbours, 'Labelled as Noise')
            	continue

            # This line is executed when data point is not labelled either as Noise or not processed yet
            self.clusterCount = self.clusterCount + 1	# Create a new cluster for this point i
            label[i] = self.clusterCount			# Assign the point this Cluster Label

            seed_set = np.setdiff1d(neighbours, [i])	# Check for Non-core and Core points
            for k in seed_set:
            	if label[k] == -1:					# if the point is labelled earlier as Noise
            		label[k] = self.clusterCount	# It now belongs to new cluster. (since it lies in eps boundary)
            	if label[k] != 0:					# if the pioint is already processed (labelled) skip that point
            		continue
            	# This line is executed when the point is either not noise or not processed yet
            	label[k] = self.clusterCount		# Label it as belonging to new cluster we created
            	other_neighbours = self.RangeQuery(data, k) # Check for neighbourhood of connected points
            	if len(other_neighbours) >= self.minPts:	# If they are more than min Points then	add them to connected points list
            		seed_set = np.append(seed_set, other_neighbours)
            # print(seed_set)
            # After this, for loop all points are labelled

        return label