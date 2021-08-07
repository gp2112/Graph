
#	Guilherme Ramos Costa Paixão - 11796079
#	Dennis Lemke Green - 112219108

# this program counts how many nodes doesn't have children

import graph

g = graph.read_pajek(input(), directed=True)

count = 0

for v in g.adj_list:
	if len(v.adj) == 0:
		count += 1

print(count)