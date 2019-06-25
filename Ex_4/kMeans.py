#!/usr/bin/env python3 
#-*- coding: utf-8 -*-
import numpy as np
def loadDataSet(fileName):
	dataMat = []
	file = open(fileName)
	for line in file.readlines():
		arrLine = line.strip().split('\t')
		dataMat.append([float(arrLine[0]), float(arrLine[1])])
	dataMat = np.mat(dataMat)
	file.close()
	return dataMat
def eucDistance(vec1,vec2):
    return np.sqrt(np.sum(np.square(vec2-vec1)))
def initCentroids(dataSet,k):
    numSamples,dim = dataSet.shape
    centroids = np.zeros((k,dim))
    for i in range(k):
        index = int(np.random.uniform(0,numSamples))
        centroids[i,:] = dataSet[index,:]
    return centroids
def kMeans(dataSet,k):
    numSamples = dataSet.shape[0]
    clusterAssement = np.mat(np.zeros((numSamples,2)))
    clusterChanged = True
    centroids = initCentroids(dataSet,k)
    while clusterChanged:
        clusterChanged = False
        for i in range(numSamples):
            minDist = 100000.0
            minIndex = 0
            for j in range(k):
                distance = eucDistance(centroids[j,:],dataSet[i,:])
                if distance<minDist :
                    minDist = distance
                    minIndex = j
            clusterAssement[i,:] = minIndex,minDist**2
            if clusterAssement[i,0]!=minIndex:
                clusterChanged = True
        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssement[:0].A==j)[0]]
            centroids[j,:] = np.mean(pointsInCluster,axis=0)
    print('Congratulations,cluster complete!')
    return centroids,clusterAssement
if __name__ == '__main__':
	dataMat = loadDataSet('testSet.txt')
	centroids, clustAssing = kMeans(dataMat, 4)
	print(centroids)
	print(clustAssing)
