
#	Guilherme Ramos Costa Paixão - 11796079
#	Dennis Lemke Green - 112219108

import graph

# this program prints all nodes that have both parents that are directed descendents by vertex 1

def transverse_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(i):
			aux = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = aux


# parents-to-child graph 
g = graph.read_pajek(input(), directed=True)


transverse_matrix(g.adj_matrix)

# child-to-parents graph
aux_g = graph.Graph(g.adj_matrix, direc=True)

g.dfs(g.adj_list[0])

for v in g.adj_list[1:]:

	if len(v.adj) > 0:
		continue

	parents = aux_g.adj_list[v.label-1].adj
	if len(parents)==2:

		# the parents having pi not Null means they were runned by DFS

		if None not in (g.adj_list[parents[0].label-1].pi, g.adj_list[parents[1].label-1].pi):
			print(v)

		# if one of them is null but be the 1 itself, and the other not be null, it must also be printed
		elif g.adj_list[parents[0].label-1] == g.adj_list[0] and g.adj_list[parents[1].label-1].pi is not None:
			print(v)
		elif g.adj_list[parents[1].label-1] == g.adj_list[0] and g.adj_list[parents[0].label-1].pi is not None:
			print(v)
