#导入模块
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#计算欧式距离
def eucDistance(vec1,vec2):
    return sqrt(sum(pow(vec2-vec1,2)))

#初始聚类中心选择
def initCentroids(dataSet,k):
    numSamples,dim = dataSet.shape
    centroids = np.zeros((k,dim))
    for i in range(k):
        index = int(np.random.uniform(0,numSamples))
        centroids[i,:] = dataSet[index,:]
    return centroids

#K-means聚类算法，迭代
def kmeanss(dataSet,k):
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
                if distance<minDist:
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

#聚类结果显示
def showCluster(dataSet,k,centroids,clusterAssement):
    numSamples,dim = dataSet.shape
    mark = ['or','ob','og','ok','^r','+r','<r','pr']
    if k>len(mark):
        print('Sorry!')
        return 1
    for i in np.xrange(numSamples):
        markIndex = int(clusterAssement[i,0])
        plt.plot(centroids[i,0],centroids[i,1],mark[i],markersize=12)
    plt.show()