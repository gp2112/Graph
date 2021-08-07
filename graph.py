# -*- coding: UTF-8 -*-

from pprint import pprint
from collections import deque
import minheap
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

# Graph's data structure and algorithms 
# implementation by Guilherme Paixão
#			   2021
#

class Graph:

	def __init__(self, adj_matrix, dists=None, direc=False):
		self.adj_matrix = adj_matrix
		self.adj_list = self.__get_adj_list()
		self.dir = direc
		self.dists = dists
		self.time=0
		self.has_cycle = False

	def __repr__(self):
		s = ''
		for row in self.adj_matrix:
			for item in row:
				s += str(item)+' '
			s+='\n'
		return s

	def __str__(self):
		s = ''
		for row in self.adj_matrix:
			for item in row:
				s += str(item)+' '
			s+='\n'
		return s

	# create the adj list given an adj matrix
	def __get_adj_list(self):
		adj1 = []
		for i, v in enumerate(self.adj_matrix):
			adj1.append(Vertice(i+1))
		for i, v in enumerate(self.adj_matrix):
			for j, dist in enumerate(v):
				if dist > 0:
					adj1[i].adj.append(adj1[j])

		return adj1

	def bfs(self, source, dest=None):
		visited = set()
		for v in self.adj_list:
			v.d = math.inf
			v.pi = None
		q = deque()
		q.append(source)
		source.d = 0

		while len(q) > 0:
			v = q.popleft()

			if v == dest:
				return True

			for u in v.adj:
				if v.d + 1 < u.d:
					u.d = v.d + 1
					u.pi = v
					q.append(u)
		return False

	def dfs(self, source, dest=None):
		visited = set()
		for v in self.adj_list:
			v.pi = None
		s = [source]
		while len(s) > 0:
			v = s.pop()
			if v in visited:
				continue
			if v == dest:
				return True
			visited.add(v)
			for u in v.adj:
				u.pi = v
				s.append(u)
		return False

	def weight(self, v, u):
		return self.adj_matrix[v.label-1][u.label-1]

	def dijkstra(self, source):

		heap = minheap.MinHeap(comp=lambda x, y: x[1] < y[1])
		d, visited = [], []
		for v in self.adj_list:
			d.append(math.inf)
			v.pi = None
			visited.append(False)
			
		d[source.label-1] = 0
		
		heap.insert((source, 0))

		while len(heap) > 0:
			(u, min_val) = heap.min_extract()
			if visited[u.label-1]:
				continue
			visited[u.label-1] = True
			for v in u.adj:
				if d[v.label-1] > min_val + self.weight(u, v):
					d[v.label-1] = min_val + self.weight(u, v)
	
					v.pi = u
					heap.insert((v, d[v.label-1]))

		return d

	def prim(self, source):

		keys = {}

		for v in self.adj_list:
			keys[v] = math.inf
			v.pi = None

		heap = minheap.MinHeap(comp=lambda x, y: x[1] < y[1], item_repr=lambda x: x[0])
		
		keys[source] = 0
		visited = set()
		
		for v in self.adj_list:
			heap.insert((v, keys[v]))

		while len(heap) > 0:
			(v, key) = heap.min_extract()
			
			if v in visited:
				continue

			visited.add(v)

			for u in v.adj:
				if u in visited:
					continue
				if u in heap and self.weight(u, v) < keys[u]:
					keys[u] = self.weight(u, v)
					u.pi = v
					heap.insert((u, keys[u]))
		
		# cria grafo da arvore minima geradora obtida e soma as arestas
		key_sum = 0
		new_graph_adj = [[0 for _ in self.adj_matrix] for _ in self.adj_matrix]
		for v in self.adj_list:
			if v.pi is not None:
				new_graph_adj[v.pi.label-1][v.label-1] = keys[v]
			key_sum += keys[v]			

		return Graph(new_graph_adj), key_sum






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
def read_pajek(file, directed=False):
	if type(file) is str:
		file = open(file, 'r')

	line = file.readline().strip()
	
	v_num = int(line.split(' ')[-1].strip())

	line = file.readline().strip()

	while line == '\n':
		line = file.readline()

	# cria os vértices
	matrix = [[0 for j in range(v_num)] for i in range(v_num)]

	line = file.readline().strip().split('    ')
	while len(line) > 1:
		edge = (int(line[0])-1, int(line[1])-1)

		# if has weight
		if len(line) == 3:
			matrix[edge[0]][edge[1]] = int(line[2])
			if not directed:
				matrix[edge[1]][edge[0]] = int(line[2])
		else:
			matrix[edge[0]][edge[1]] = 1
			if not directed:
				matrix[edge[1]][edge[0]] = 1

		line = file.readline().strip().split('    ')

	file.close()

	return Graph(adj_matrix=matrix)
