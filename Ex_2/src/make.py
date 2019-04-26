from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import os
import sys

def load_words(data="../data/segmented.txt"):
	file = open(data, "r", encoding='UTF-8')
	lines = file.readlines()
	array = []
	for line in lines:
		array.append(line)
	file.close()
	return array
def load_class(data="../data/class.txt"):
	array = []
	file = open(data,"r", encoding='UTF-8')
	lines = file.readlines()
	for line in lines:
		array.append(int(line))
	file.close()
	return array
def main():
	train_data, test_data, train_y, test_y = train_test_split(load_words(),load_class(),test_size=0.33,shuffle=True)
	vectorizer = CountVectorizer()
	wordX = vectorizer.fit_transform(train_data)
	clf = MultinomialNB().fit(wordX, train_y)
	test_wordX = vectorizer.transform(test_data).toarray()
	predicted = clf.predict(test_wordX)
	class_target = ['Normal', 'Insult']
	print(classification_report(test_y,predicted,target_names=class_target))
	print('accuracy: ',accuracy_score(test_y, predicted))

if __name__ == '__main__':
	for i in range(10):
		main()
	os.system("pause")