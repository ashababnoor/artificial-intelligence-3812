import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from numpy.lib.function_base import append

datapath = 'k-means_clustering/datasets/'
mydata = genfromtxt((datapath+'data.csv'), delimiter=',')
# taking centers from main dataset
mycenters = mydata[:6]

# for plotting different points
colors = ['#007bff', '#6f42c1', '#dc3545', '#fd7e14', '#ffc107', '#28a745']

# # plotting the initial data position
# x = [data[0] for data in mydata]
# y = [data[1] for data in mydata]
# plt.scatter(x, y, s=10, c='blue')

# # plotting the initial centers
# x = [center[0] for center in mycenters]
# y = [center[1] for center in mycenters]
# plt.scatter(x, y, s=20, c='black', edgecolors='black', linewidth=1)


clusters = []
for i in range(len(mycenters)):
    clusters.append([])

centers = mycenters.copy()

def plot_points(clusters, centers, iteration=0, state=0, colors=colors):
    plt.cla()
    total_data = 0

    '''plotting the data points'''
    if len(clusters) > 6:
        x = [data[0] for data in clusters]
        y = [data[1] for data in clusters]
        label_text = ''
        plt.scatter(x, y, s=25, c='#555555', alpha=0.5, label = label_text)
        total_data = len(clusters)
    else:
        for ind, cluster in enumerate(clusters):
            x = [mydata[i][0] for i in cluster]
            y = [mydata[i][1] for i in cluster]
            label_text = 'Cluster '+str(ind+1)
            plt.scatter(x, y, s=25, c=colors[ind], alpha=0.65, label = label_text)
            total_data += len(cluster)

    '''plotting the centers'''
    x = [center[0] for center in centers]
    y = [center[1] for center in centers]
    plt.scatter(x, y, s=120, c=colors, edgecolors='black', alpha=0.8, linewidth=2, marker='D', label='Centers')

    # plt.legend(loc='upper center') 
    title_text = 'K-Means Clustering - (K = ' + str(len(centers)) + ', data = ' + str(total_data) + ')\n'
    if state == 1:
        title_text += 'Iter ' + str(iteration) + ': ' + 'Assigning data to centroids'
    elif state == 2:
        title_text += 'Iter ' + str(iteration) + ': ' + 'Updating centroids'

    plt.title(title_text)
    fig_name = 'k-means_clustering/cluster_images/version-02/plot_' + str(iteration + 100) + '_' + str(state) + '.png'
    plt.savefig(fig_name)

# plotting initial state
plot_points(mydata, centers)

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

    # plotting points after assigning to centroids
    plot_points(temp_clusters, centers, iteration+1, state=1)

    for cluster in temp_clusters:
        array = np.mean(np.array([mydata[ind] for ind in cluster]), axis=0)
        centers = centers[1:]
        centers = np.append(centers, [array], axis=0)

    # plotting points after updating centroids
    plot_points(temp_clusters, centers, iteration+1, state=2)

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

        if shift < 1:
            clusters = temp_clusters
            break

    clusters = temp_clusters


#final plot
plt.cla()

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

plt.legend(loc='upper center')
plt.title('K-means Clustering')

# plt.savefig('k-means_clustering/plot-proper-clusters.png')

print('Number of iterations needed:', iteration)

# plt.show()
