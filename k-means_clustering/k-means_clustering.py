import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from numpy.lib.function_base import append

datapath = 'k-means_clustering/datasets/'
mydata = genfromtxt((datapath+'data.csv'), delimiter=',')
mycenters = genfromtxt((datapath+'centers.csv'), delimiter=',')


# # plotting the initial data position
# x = [data[0] for data in mydata]
# y = [data[1] for data in mydata]
# plt.scatter(x, y, s=10, c='blue')

# # plotting the initial centers
x = [center[0] for center in mycenters]
y = [center[1] for center in mycenters]
plt.scatter(x, y, s=20, c='black', edgecolors='black', linewidth=1)


clusters = []
for i in range(len(mycenters)):
    clusters.append([])

centers = mycenters.copy()
# print('original centers: \n', centers)


iteration = 0

while True:
    temp_clusters = []
    for i in range(len(mycenters)):
        temp_clusters.append([])

    for data in range(len(mydata)):
        index = 0
        min_dist = np.sum(np.square(mydata[data] - centers[0]))
        for center in range(1, len(centers)):
            distance = np.sum(np.square(mydata[data] - centers[center]))
            if distance < min_dist:
                min_dist = distance
                index = center
        
        temp_clusters[index].append(data)
    
    # sub_iter = 1
    for cluster in temp_clusters:
        array = np.mean(np.array([mydata[ind] for ind in cluster]), axis=0)
        centers = centers[1:]
        centers = np.append(centers, [array], axis=0)
        # print('\n After iter', sub_iter)
        # print(centers)
        # print('new is:', array)
        # sub_iter += 1

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

# for plotting different points
colors = ['#007bff', '#6f42c1', '#dc3545', '#ffc107', '#fd7e14', '#28a745']

# plotting the data points
for ind, cluster in enumerate(clusters):
    x = [mydata[i][0] for i in cluster]
    y = [mydata[i][1] for i in cluster]
    label_text = 'Cluster '+str(ind+1)
    plt.scatter(x, y, s=20, c=colors[ind], alpha=0.7, label = label_text)

# plotting the centers
x = [center[0] for center in centers]
y = [center[1] for center in centers]

plt.scatter(x, y, s=150, c='black', edgecolors='black', alpha=0.7, linewidth=1, marker='*', label='Centers')
plt.legend()

plt.title('K-means Clustering')
plt.suptitle('Hello')

# plt.savefig('k-means_clustering/plot.png')

print('Number of iterations needed:', iteration)

plt.show()

