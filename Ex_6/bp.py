#!/usr/bin/env python3
#-*-coding:utf-8-*-
import math
import random
random.seed(0)
def rand(a,b):
	return (b-a)*random.random()+a;

def make_matrix(m,n,fill=0.0):
	# 创建一个指定大小的矩阵，使用fill值填充
	mat = []
	for i in range(m):
		mat.append([fill]*n)
	return mat
	
def sigmoid(x):
	return 1.0/(1.0+math.exp(-x))
	

def sigmoid_deriviate(x):
	return x*(1-x)
class BPNN:
	def __init__(self):
		self.input_n = 0
		self.hidden_n = 0
		self.output_n = 0
		self.input_cells = []
		self.hidden_cells = []
		self.output_cells = []
		self.input_weights = []
		self.output_weights = []
	def setup(self,ni,nh,no):
		self.input_n = ni + 1
		self.hidden_n = nh
		self.output_n = no
		self.input_cells = [1.0]*self.input_n
		self.hidden_cells = [1.0]*self.hidden_n
		self.output_cells = [1.0]*self.output_n
		self.input_weights = make_matrix(self.input_n,self.hidden_n)
		self.output_weights = make_matrix(self.hidden_n, self.output_n)
		for i in range(self.input_n):
			for h in range(self.hidden_n):
				self.input_weights[i][h]=rand(-0.2,0.2)
		for h in range(self.hidden_n):
			for o in range(self.output_n):
				self.output_weights[h][o] = rand(-2.0, -2.0)
	def predict(self,inputs):
		for i in range(self.input_n - 1):
			self.input_cells[i] = inputs[i]
		
		for h in range(self.hidden_n):
			total = 0.0
			for i in range(self.input_n):
				total += self.input_cells[i]*self.input_weights[i][h]
			self.hidden_cells[h] = sigmoid(total)
		for k in range(self.output_n):
			total=0.0
			for j in range(self.hidden_n):
				total += self.hidden_cells[j] * self.output_weights[j][k]
			self.output_cells[k] = sigmoid(total)
		return self.output_cells[:]
	
	def back_propagate(self,case,label,learning_rate):
		self.predict(case)
		output_error = [0.0]*self.output_n
		for o in range(self.output_n):
			error = label[o] - self.output_cells[o]
			output_error[o] = error * sigmoid_deriviate(self.output_cells[o])
		hidden_error = [0.0]*self.hidden_n
		for h in range(self.hidden_n):
			error = 0.0
			for o in range(self.output_n):
				error+=output_error[o]*self.output_weights[h][o]
			hidden_error[h] = error * sigmoid_deriviate(self.hidden_cells[h])
		for h in range(self.hidden_n):
			for o in range(self.output_n):
				change = output_error[o]*self.hidden_cells[h]
				self.output_weights[h][o] += learning_rate * change
		
		for i in range(self.input_n):
			for h in range(self.hidden_n):
				change = hidden_error[h]*self.input_cells[i]
				self.input_weights[i][h]+=learning_rate*change
		global_error = 0.0
		for o in range(self.output_n):
			global_error += 0.5*(label[o] - self.output_cells[o])**2
		return global_error
	
	# 定义训练函数
	def train(self,cases,labels,limit=10000,lr=0.1):
		for i in range(limit):
			error = 0.0
			for j in range(len(cases)):
				label = labels[j]
				case = cases[j]
				error+=self.back_propagate(case, label, lr)
					

	def test(self):
		cases = [[0,0],
			   [0,1],
			   [1,0],
			   [1,1]]
		labels = [[0],[1],[1],[0]]
		self.setup(2,5,1)
		self.train(cases,labels)
		for case in cases:
			print(self.predict(case))
if __name__ == '__main__':
	nn = BPNN()
	nn.test()

