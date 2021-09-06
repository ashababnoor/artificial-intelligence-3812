import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

datapath = 'k-means_clustering/datasets/'
mydata = genfromtxt((datapath+'data.csv'), delimiter=',')
mycenters = genfromtxt((datapath+'centers.csv'), delimiter=',')

# print(mydata.shape)
# print(mycenters.shape)

clusters = []
temp_clusters = []

for i in range(6):
    clusters.append([])
    temp_clusters.append([])

# print(clusters)
# print(temp_clusters)

centers = mycenters.copy()

iteration = 0

while True:
    for data in range(len(mydata)):
        index = 0
        min_dist = np.sum(np.square(mydata[data] - centers[0]))
        for center in range(1, len(centers)):
            distance = np.sum(np.square(mydata[data] - centers[center]))
            if distance < min_dist:
                min_dist = distance
                index = center
        
        temp_clusters[index].append(data)

    for cluster in temp_clusters:
        array = np.array([mydata[ind] for ind in cluster])
        centers = centers[1:]
        




