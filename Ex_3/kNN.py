#coding=utf-8
from numpy import *  #科学计算包numpy
import operator      #运算符模块
#k-近邻算法
#计算距离
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]   #shape读取数据矩阵第一维度的长度
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  #tile重复数组inX，有dataSet行 1个dataSet列，减法计算差值
    sqDiffMat=diffMat**2 #**是幂运算的意思，这里用的欧式距离
    sqDisttances=sqDiffMat.sum(axis=1) #普通sum默认参数为axis=0为普通相加，axis=1为一行的行向量相加
    distances=sqDisttances**0.5
    sortedDistIndicies=distances.argsort() #argsort返回数值从小到大的索引值（数组索引0,1,2,3）
 #选择距离最小的k个点
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]] #根据排序结果的索引值返回靠近的前k个标签
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1 #各个标签出现频率
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) #排序频率
    #!!!!!  classCount.iteritems()修改为classCount.items()
    #sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list。
    # reverse默认升序 key关键字排序itemgetter（1）按照第一维度排序(0,1,2,3)
    return sortedClassCount[0][0]  #找出频率最高的


def file2matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines) #读出数据行数
    returnMat=zeros((numberOfLines,3))  #创建返回矩阵
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()  #删除空白符
        listFromLine=line.split('\t') #split指定分隔符对数据切片
        returnMat[index,:]=listFromLine[0:3] #选取前3个元素（特征）存储在返回矩阵中
        classLabelVector.append(int(listFromLine[-1]))
        #-1索引表示最后一列元素,位label信息存储在classLabelVector
        index+=1
    return returnMat,classLabelVector

#归一化特征值
#归一化公式  ：（当前值-最小值）/range
def autoNorm(dataSet):
    minVals=dataSet.min(0) #存放每列最小值，参数0使得可以从列中选取最小值，而不是当前行
    maxVals=dataSet.max(0) #存放每列最大值
    ranges = maxVals - minVals
    normDataSet=zeros(shape(dataSet))  #初始化归一化矩阵为读取的dataSet
    m=dataSet.shape[0]  #m保存第一行
    # 特征矩阵是3x1000，min max range是1x3 因此采用tile将变量内容复制成输入矩阵同大小
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet, ranges, minVals




import os, sys
def img2vector(filename):
    returnVect=zeros((1,1024))#每个手写识别为32x32大小的二进制图像矩阵 转换为1x1024 numpy向量数组returnVect
    fr=open(filename)#打开指定文件
    for i in range(32):#循环读出前32行
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])#将每行的32个字符值存储在numpy数组中
    return returnVect

#测试算法
def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = os.listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("分类器识别的结果: %d, 正确的结果: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print("错误总数是: %d" % errorCount)
    print("错误率是: %f" % (errorCount / float(mTest)))

handwritingClassTest()  #手写识别测试