import jieba
import sys
import re
from string import punctuation
def devidewords(input, output):
	if sys.getdefaultencoding()!='utf-8':
		reload(sys)
		sys.setdefaultencoding('utf-8')

	add_punc = '，。、【】“”：（）《》‘’「」？！～……$%^@#¥{}[]<>=————-.'
	all_punc = add_punc+punctuation

	f1 = open(input,"r")
	f2 = open(output, "w")
	f2.close()
	lines = re.sub('[\n]+','\n',f1.read()).split("\n")
	for line in lines:
		seg = jieba.cut(line.strip(), cut_all=False)
		s = ' '.join(seg)
		m = list(s)
		for i in m:
			if i in all_punc:
				m.remove(i)
			if i=="\n":
				m.remove(i)
		m.append("\n")
		for word in m:
			f = open(output,"ab+")
			f.write(word.encode('UTF-8'))
			f.close()
	f1.close()
