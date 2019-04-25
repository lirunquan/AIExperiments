import numpy as np
def loadDataSet():
	postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
      			['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
    			['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
     			['stop', 'posting', 'stupid', 'worthless', 'garbage'],
     			['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
     			['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
	classVec=[0,1,0,1,0,1]
	return postingList,classVec
def createVocabList(dataSet):
	vocabSet=set([])
	for document in dataSet:
		vocabSet=vocabSet|set(document)
	return list(vocabSet)
def setOfWords2Vec(vocabList, inputSet):
	returnVec=np.zeros(len(vocabList))
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)]=1
		else:
			print('the word %s is not in my Vacabulary'%word)
	return returnVec
def classifyNB(vec2classify,p0Vec,p1Vec,pClass1):
	p1=sum(vec2classify*p1Vec)+np.log(pClass1)
	p0=sum(vec2classify*p0Vec)+np.log(1-pClass1)
	if p1>p0:
		return 1
	else:
		return 0
def trainNB1(trainMatrix,trainCategory):
	numTrainDoc=len(trainMatrix)
	numWord=len(trainMatrix[0])
	pAbusive=sum(trainCategory)/float(numTrainDoc)
	p0Num=np.ones(numWord)
	p1Num=np.ones(numWord)
	p0Denom=2.0
	p1Denom=2.0
	for i in range(numTrainDoc):
		if trainCategory[i]==1:
			p1Num+=trainMatrix[i]
			p1Denom+=sum(trainMatrix[i])
		else:
			p0Num+=trainMatrix[i]
			p0Denom+=sum(trainMatrix[i])
	p1Vec=np.log(p1Num/p1Denom)
	p0Vec=np.log(p0Num/p0Denom)
	return p0Vec,p1Vec,pAbusive

def testingNB():
	listPosts,listClasses=loadDataSet()
	myVocabList=createVocabList(listPosts)
	train=[]
	for postinDoc in listPosts:
		train.append(setOfWords2Vec(myVocabList,postinDoc))
	p0V,p1V,pAb=trainNB1(train,listClasses)
	testEntry=['love','ate','dog']
	thisDoc=setOfWords2Vec(myVocabList,testEntry)
	print(testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb))
	testEntry=['stupid','steak']
	thisDoc=np.array(setOfWords2Vec(myVocabList,testEntry))
	print(testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb))
testingNB()

