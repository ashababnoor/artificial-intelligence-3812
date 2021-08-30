import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

datapath = 'k-means_clustering/datasets/'
mydata = genfromtxt((datapath+'data.csv'), delimiter=',')
mycenters = genfromtxt((datapath+'centers.csv'), delimiter=',')

# print(mydata.shape)
# print(mycenters.shape)

