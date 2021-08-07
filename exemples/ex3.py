
#	Guilherme Ramos Costa Paixão - 11796079
#	Dennis Lemke Green - 112219108

import graph


#vs = []

def transverse_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(i):
			aux = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = aux


# grafo de pais para filhos
g = graph.read_pajek(input(), directed=True)
#print(g)

transverse_matrix(g.adj_matrix)

# grafo de filhos para pais
aux_g = graph.Graph(g.adj_matrix, direc=True)
#print(aux_g)

g.dfs(g.adj_list[0])

for v in g.adj_list[1:]:

	if len(v.adj) > 0:
		continue

	parents = aux_g.adj_list[v.label-1].adj
	if len(parents)==2:
		#print(v, parents)
		#print(g.adj_list[parents[0].label-1].pi, g.adj_list[parents[1].label-1].pi)
		#print("===============")

		# se os pais possuem pi, ou seja, antecessor, não nulo, significa que foram percorridos no DFS
		if None not in (g.adj_list[parents[0].label-1].pi, g.adj_list[parents[1].label-1].pi):
			print(v)

		## Se um deles for nulo, mas for o próprio 1, e o outro não for nulo, também deve ser impresso
		elif g.adj_list[parents[0].label-1] == g.adj_list[0] and g.adj_list[parents[1].label-1].pi is not None:
			print(v)
		elif g.adj_list[parents[1].label-1] == g.adj_list[0] and g.adj_list[parents[0].label-1].pi is not None:
			print(v)
