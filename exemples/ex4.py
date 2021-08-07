
#	Guilherme Ramos Costa Paixão - 11796079
#	Dennis Lemke Green - 112219108

import math
import graph


def transverse_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(i):
			aux = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = aux


def min_dist(g):
	min_ = math.inf
	for v in g.adj_list:
		if v.d < min_:
			pass

# grafo de pais para filhos
g = graph.read_pajek(input(), directed=True)

transverse_matrix(g.adj_matrix)

# grafo de filhos para pais
aux_g = graph.Graph(g.adj_matrix, direc=True)

g.dfs(g.adj_list[0])


vertices_c = []



# pega os vértices da C
for v in g.adj_list[1:]:

	if len(v.adj) > 0:
		continue

	parents = aux_g.adj_list[v.label-1].adj
	if len(parents)==2:

		# se os pais possuem pi, ou seja, antecessor, não nulo, significa que foram percorridos no DFS
		if None not in (g.adj_list[parents[0].label-1].pi, g.adj_list[parents[1].label-1].pi):
			vertices_c.append(v)

		## Se um deles for nulo, mas for o próprio 1, e o outro não for nulo, também deve ser impresso
		elif g.adj_list[parents[0].label-1] == g.adj_list[0] and g.adj_list[parents[1].label-1].pi is not None:
			vertices_c.append(v)
		elif g.adj_list[parents[1].label-1] == g.adj_list[0] and g.adj_list[parents[0].label-1].pi is not None:
			vertices_c.append(v)


# Realiza o BFS para pegar as distancias de cada vertice para o 1

g.bfs(g.adj_list[0])


# busca a suma mínima das distancias dos pais para o vertice 1
min_ = math.inf
for v in vertices_c:
	if len(aux_g.adj_list[v.label-1].adj) == 2:
		parents = (aux_g.adj_list[v.label-1].adj[0], aux_g.adj_list[v.label-1].adj[1])
		s = g.adj_list[parents[0].label-1].d + g.adj_list[parents[1].label-1].d
		if s < min_:
			min_ = s


for v in vertices_c:
	parents = (aux_g.adj_list[v.label-1].adj[0], aux_g.adj_list[v.label-1].adj[1])

	# verifica se a distancia dos pais para o 1 é mínima
	if g.adj_list[parents[0].label-1].d + g.adj_list[parents[1].label-1].d == min_:
		print(v)
	

