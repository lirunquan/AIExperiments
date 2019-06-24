#!/usr/bin/env python3
#-*-coding:utf-8-*-
	import math
	import random
	random.seed(0)
	①首先添加几个工具函数。
	def rand(a,b):
		return (b-a)*random.random()+a;

	def make_matrix(m,n,fill=0.0):
		# 创建一个指定大小的矩阵，使用fill值填充
		mat = []
		for i in range(m):
			mat.append([fill]*n)
		return mat
	
②实现激活函数sigmoid及其一阶导数。公式见前面。
def sigmoid(x):
	# e的n次方可以这样写：math.exp(n)
	# 记得return语句，记得使用1.0而不是1
	#【代码待补全】
	

def sigmoid_deriviate(x):
	# 注意这里的参数x已经是sigmoid函数的输出
	#【代码待补全】

③定义BPNN类。在类中实现BP算法的前馈、反向传播以及参数的更新。
class BPNN:
	# 注意每边都是两个下划线
	# 初始化一些变量
	def __init__(self):
		# 下面三个变量保存各层神经元个数
		self.input_n = 0
       		self.hidden_n = 0
       		self.output_n = 0
# 下面三个变量保存各层神经元的输出值
self.input_cells = []
self.hidden_cells = []
self.output_cells = []
# 下面两个变量保存权重
self.input_weights = []
self.output_weights = []
		
		# 初始化神经网络
		def setup(self,ni,nh,no):
			# ni,nh,no分别代表输入层、隐含层、输出层
			# 的神经元个数
			# 注意这里只对隐含层的神经元增加偏置值
			# 处理方式是在输入层增加一个神经元，使
			# 其统一到权重之中。
			self.input_n = ni + 1
			self.hidden_n = nh
			self.output_n = no
			# 初始化每一层神经元的值为1
			# 之所以设为1是为了将偏置值看作是输入恒为1的
			# 神经元与其它神经元的连接的权重
			self.input_cells = [1.0]*self.input_n
			# 仿照上面的代码初始化隐含层和输出层的神经元
			#【代码待补全】

			# 初始化权重
			self.input_weights = \
make_matrix(self.input_n,self.hidden_n)
for i in range(self.input_n):
	for h in range(self.hidden_n):
		self.input_weights[i][h]=\
			rand(-2.0,2.0)
		# 仿照上面的代码初始化隐含层到输出层的权重
			#【代码待补全】
		
# 编写predict函数进行一次前馈，返回输出
		def predict(self,inputs):
			# 根据用户提供的输入填充输入层的数据
			for i in range(self.input_n - 1):
				#【思考】这里为什么要减一？
				self.input_cells[i] = inputs[i]
			
			# 根据输入层的数据前向计算隐含层的值
			for h in range(self.hidden_n):
				total = 0.0
				for i in range(self.input_n):
					# 计算W*a
					total += self.input_cells[i]*\
							self.input_weights[i][h]
				# 调用激活函数
				self.hidden_cells[h] = sigmoid(total)

			# 根据隐含层的数据前向计算输出层的值
			# 仿照前面的代码完成这一步骤
			#【代码待补全】

			# 返回网络输出
			return self.output_cells[:]
		
		#执行一次反向传播和权值更新，并返回预测的误差
		def back_propagate(self,case,label,learning_rate):
			# case和label分别是训练数据及期望输出
			# learning_rate为学习率
			# 前向传播填充各层数据
			self.predict(case)
			# 获取输出层误差
			output_error = [0.0]*self.output_n
			for o in range(self.output_n):
				error = label[o] - self.output_cells[o]
				output_error[o] = error * \
					sigmoid_deriviate(self.output_cells[o])
			# 获取隐含层误差
			hidden_error = [0.0]*self.hidden_n
			for h in range(self.hidden_n):
				error = 0.0
				for o in range(self.output_n):
					# 根据公式计算error
					#【代码待补全】

				hidden_error[h] = error * \
					sigmoid_deriviate(self.hidden_cells[h])
			
			# 更新隐含层到输出层权值
			for h in range(self.hidden_n):
				for o in range(self.output_n):
					change = output_error[o]*self.hidden_cells[h]
					self.output_weights[h][o] += \
						learning_rate * change
			
			# 更新输入层到隐含层权值
			# 仿照前面的代码以及权值更新公式完成代码
			#【代码待补全】

			# 返回全局误差
			# 全局误差公式为
			# E=1/2 ∑_i^n▒〖(T_i-O_i)〗^2 
			global_error = 0.0
			for o in range(self.output_n):
				global += 0.5*(label[o] - \
self.output_cells[o])**2
			return global_error
		
		# 定义训练函数
		def train(self,cases,labels,limit=10000,lr=0.1):
			# limit代表迭代次数，lr是学习率
			for i in range(limit):
				error = 0.0
				for j in range(len(cases)):
					label = labels[j]
					case = cases[j]
					# 调用反向传播函数，累加误差
					# 当迭代次数是1000的倍数时打印误差
					#【代码待补全】
					

		# 定义测试函数，目的是学习异或逻辑
		def test(self):
			# 训练数据
			cases = [[0,0],
				   [0,1],
				   [1,0],
				   [1,1]]
			labels = [[0],[1],[1],[0]]
			self.setup(2,5,1)
			self.train(cases,labels)
			for case in cases:
				print(self.predict(case))
	
	④添加如下代码到文件末尾
	if __name__==’__main__’:
nn = BPNN()
nn.test()

