import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from numpy.lib.function_base import append

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
print('original centers:', centers)
print()

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
    
    sub_iter = 1
    for cluster in temp_clusters:
        array = np.mean(np.array([mydata[ind] for ind in cluster]), axis=0)
        centers = centers[1:]
        centers = np.append(centers, [array], axis=0)
        # print('\n After iter', sub_iter)
        # print(centers)
        # print('new is:', array)
        sub_iter += 1

    iteration += 1    
    if iteration > 1:
        shift = 0
        for data in range(len(mydata)):
            cluster_ind = None
            temp_ind = None
            for ind, cluster in enumerate(clusters):
                if data in cluster:
                    cluster_ind = ind
            for ind, cluster in enumerate(temp_clusters):
                if data in cluster:
                    temp_ind = ind
            if temp_ind != cluster_ind:
                shift += 1

        if shift < 10:
            clusters = temp_clusters
            break
    clusters = temp_clusters


plt.plot(centers)
plt.show()

