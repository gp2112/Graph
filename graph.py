# -*- coding: UTF-8 -*-

from pprint import pprint
from collections import deque
import random
import math

WHITE = 0
GREY = 1
BLACK = 2

class Vertice:

	def __init__(self, label, adj=None):
		if adj is None: 
			adj = []
		self.adj = adj
		self.label = label
		self.cor = WHITE
		self.pi = None

	def __repr__(self):
		return str(self.label)

class Graph:

	def __init__(self, adj_matrix, direc=False):
		self.adj_matrix = adj_matrix
		self.adj_list = self.__get_adj_list()
		self.dir = direc
		self.time=0

	def __repr__(self):
		return self.adj_matrix

	def __str__(self):
		return str(self.adj_matrix)

	# cria lista de adjacência com base na matriz de adjacencia
	def __get_adj_list(self):
		adj1 = []
		for i, v in enumerate(self.adj_matrix):
			adj1.append(Vertice(i+1))
		for i, v in enumerate(self.adj_matrix):
			for j, dist in enumerate(v):
				if dist > 0:
					adj1[i].adj.append(adj1[j])

		return adj1

	# do BFS with a vertex S as origin
	def __bfs(self, s):
		if type(s) is int:
			s = self.adj_list[s-1]
		for u in self.adj_list:
			if u != s:
				u.d = math.inf
		s.cor = GREY
		s.d = 0
		s.pi = None
		q = deque()
		q.append(s)
		while len(q) > 0:
			u = q.popleft()
			for v in self.adj_list[u.label-1].adj:
				if v.cor == WHITE:
					v.cor = GREY
					v.d = u.d + 1
					v.pi = u
					q.append(v)
			u.cor = BLACK


	def __dfs_visit(self, u, count):
		count+=1
		self.time += 1
		u.d = self.time
		u.cor = GREY
		for v in u.adj:
			if v.cor == WHITE:
				v.pi = u
				count = self.__dfs_visit(v, count)
		u.cor = BLACK
		self.time += 1
		u.f = self.time
		return count


	def dfs(self):
		for u in self.adj_list:
			if u.cor == WHITE:
				self.__dfs_visit(u, 0)

	# retorna o número de componentes do grafo com DFS
	def coponentes(self):
		c = []
		for u in self.adj_list:
			u.pi = None
		c.append(self.adj_list[0])
		self.adj_list[0].count = self.__dfs_visit(self.adj_list[0], 0)
		for v in self.adj_list:
			if v.cor != BLACK:
				v.count = self.__dfs_visit(v, 0)
				c.append(v)
		return c



	# print recursively the path between source and dest
	# returns True if path exists, False if doesn't
	def __recur_min_path(self, source, dest):
		if dest.d == math.inf:
			return False

		print(dest)
		if source == dest:
			return True
		return self.__recur_min_path(source, dest.pi)

	# imprime o caminho mínimo entre os vértices source e dest
	def min_path(self, source, dest):
		source = self.adj_list[source-1]
		dest = self.adj_list[dest-1]
		self.__bfs(source)
		return self.__recur_min_path(source, dest)

	# retorna a distância do menor caminho entre os vértices source e dest
	def dist(self, source, dest):
		source = self.adj_list[source-1]
		dest = self.adj_list[dest-1]
		self.__bfs(source)
		return dest.d

# returns a random graph using Erdos algorithm
# n is the number of vertex and p is probability 
def erdos_graph(n, p):
	if p <= 0 or p >= 1:
		raise Exception('P must be in (0, 1) range')
	matrix = deque([[0 for j in range(n)] for i in range(n)]) 
	
	for i in range(n):
		for j in range(i):
			x = random.random()
			if x > p:
				matrix[i][j] = 1
				matrix[j][i] = 1
	return Graph(matrix)

# read a graph from .pajek file
def read_pajek(file, dists=None):
	if type(file) is str:
		file = open(file, 'r')

	line = file.readline()
	v_num = int(line.split(' ')[-1].strip())

	line = file.readline()

	while line == '\n':
		line = file.readline()

	# cria os vértices
	matrix = [[0 for j in range(v_num)] for i in range(v_num)]
	
	line = file.readline().strip().split(' ')
	while len(line) > 1:
		edge = (int(line[0])-1, int(line[1])-1)

		matrix[edge[0]][edge[1]] = 1
		matrix[edge[1]][edge[0]] = 1

		line = file.readline().strip().split(' ')

	file.close()

	return Graph(adj_matrix=matrix)

if __name__ == '__main__':
	fname = input()
	g = read_pajek(fname)
	componentes = g.coponentes()
	componentes.sort(reverse=True, key=lambda c: c.count)
	print(len(componentes))
	for componente in componentes:
		print(componente.count)
