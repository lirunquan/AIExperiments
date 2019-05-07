#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

iris = datasets.load_iris()
def predicted_result(n):
	x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.33,random_state=45)
	ss = StandardScaler()
	x_train = ss.fit_transform(x_train)
	x_test = ss.transform(x_test)
	knn = KNeighborsClassifier(n_neighbors=n)	
	knn.fit(x_train, y_train)
	y_predict = knn.predict(x_test)
	label = iris.target_names
	#for i in range(len(y_predict)):
		#print("Test %02d: truth:[%s]    \tpredicted:[%s]"%((i+1),label[y_predict[i]],label[y_test[i]]))
	print("Accuracy with KNN(k=%d): %f"%(n,knn.score(x_test,y_test)))
def cross():
	x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.33,random_state=45)
	params = {'n_neighbors': [2,3,4,5]}
	knn = KNeighborsClassifier()	
	gcv = GridSearchCV(knn, param_grid=params, cv=3)
	gcv.fit(x_train, y_train)
	print("Cross Validation Accuracy: ",gcv.score(x_test, y_test))
	print("Best Result in Cross Validation: ",gcv.best_score_)
	print("Best estimator: ",gcv.best_estimator_)

if __name__ == '__main__':
	for i in [2,3,4,5]:
		predicted_result(i)
	cross()