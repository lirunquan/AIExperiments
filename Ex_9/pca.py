import numpy as np
import matplotlib.pyplot as plt
def loadDataSet(filename):
	fr = open(filename)
	stringArr = [line.strip().split('\t') for line in fr.readlines()]
	dataArr = [list(map(float,line)) for line in stringArr]
	fr.close()
	return np.mat(dataArr)
def getNumOfFeat(eigVals,percentage):
    sortArray = np.sort(eigVals)       
    sortArray = sortArray[-1::-1]   
    arraySum = sum(sortArray)       
    tempSum = 0
    num = 0
    for i in sortArray:
        tempSum+=i
        num+=1
        if tempSum>=arraySum*percentage:
            return num

def pca(dataMat,percentage=0.9):
    meanVals = np.mean(dataMat,axis=0)                 
    meanRemoved = dataMat-meanVals
    covMat = np.cov(meanRemoved,rowvar=0)              
    eigVals,eigVects = np.linalg.eig(np.mat(covMat))      
    k = getNumOfFeat(eigVals,percentage)               
    eigVallnd = np.argsort(eigVals)                    
    eigVallnd = eigVallnd[:-(k+1):-1]               
    redEigVects = eigVects[:,eigVallnd]             
    lowDDataMat = meanRemoved*redEigVects           
    reconMat = (lowDDataMat*redEigVects.T)+meanVals 
    return lowDDataMat,reconMat

def test(percentage=0.9):
    dataMat = loadDataSet('testSet.txt')
    lowDMat, reconMat = pca(dataMat, percentage)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:,0].flatten().A[0],dataMat[:,1].flatten().A[0],marker='^',s=90)
    ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='o',s=50,c='red')
    plt.show()
    print('Low dimension shape is',np.shape(lowDMat),'original shape is',np.shape(reconMat))

if __name__ == '__main__':
    test(0.5)