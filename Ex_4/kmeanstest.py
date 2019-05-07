#导入模块
import kmeans
import  numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#从文件加载数据集
dataSet=[]
fileIn = open('./testSet.txt')
for line in fileIn.readline():
    lineArr = line.strip().split('\t')
    dataSet.append([float(lineArr[0]),float(lineArr[1])])

#调用k-means进行数据聚类
dataSet = np.mat(dataSet)
k = 4
centroids,clusterAssement = kmeans.kmeanss(dataSet,k)

#显示结果
kmeans.showCluster(dataSet,centroids,clusterAssement)