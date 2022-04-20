#Kmeans file
###Parameters:
#Data Matrix
#Number of Clusters k
#convergence parameter e

###Returns:
#means
#clusters found
#If point is equidistant to 2 clusters, add it to cluster with lower index

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

import random
import math

#Get distance between 2 points
def distance(mean_point, distance_point):
    return math.sqrt(sum([(mean_point[index] - distance_point[index]) ** 2 for index in range(len(mean_point))]))

#Create Random starting values for kmeans
def randomize(ranges, k):
    output = []
    while k > 0:
        output.append(tuple([random.uniform(ranges[column][0], ranges[column][1]) for column in range(len(ranges))]))
        k -= 1
    return output

#Find mean based on index subset
def mean(matrix, indexes):
    array = list(zip(*[list(matrix[index, :]) for index in indexes]))
    array = [list(item) for item in array]
    return tuple([sum(index)/len(index) for index in array])

#Return index of closest point in cluster points to point(used to find closest cluster)
def closest(cluster_points, point):
    distances = [distance(cluster_point, point) for cluster_point in cluster_points]
    return distances.index(min(distances))

#Uses Kmeans Algorithm to return cluster points and matrix row indexes in each cluster
def kmeans(matrix, k = 2, e = 10000):
    ranges = [(min(matrix[:,column]), max(matrix[:,column]))  for column in range(len(matrix[0]))]
    start_points = []
    end_points = randomize(ranges, k)
    clusters = []
    while start_points != end_points and e > 0:
        start_points = end_points
        clusters = [[] for index in range(k)]
        for row in range(len(matrix)):
            clusters[closest(start_points, tuple(matrix[row]))].append(row)
        end_points = [mean(matrix, item) for item in clusters]
        e -= 1
    return end_points, clusters

#Testing Space
D, labels = make_blobs(n_samples=500, centers=3, cluster_std=.3, random_state=0)

D.shape

clusters, values = kmeans(D)
print(clusters)
print(values)
