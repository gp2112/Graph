## About
A graph implementation in Python for Graph's class

## How to use?

### Getting a graph from a pajek file
```python
import graph

file_name = input()

g = graph.pajek_read(file_name)


```

### Depth-First Search

```python

g.bfs(source) # do DFS from vertex Source

g.bfs(source, dest=dest) # do DFS from vertex Source and, 
                          # when it passes throught vertex dest, it returns True and stop the search

```

### Breadth-First Search 

```python

g.bfs(source) # Do BFS from vertex Source

g.bfs(source, dest=dest) # Do BFS from vertex Source and, as DFS, 
                         # returns True and stop the search when hits vertex dest
```

### Dijkstra (minimum weighted paths)

```python

dists = g.dijkstra(source) # return all minimum distances betwheen source vertex when all others

```
### Prim (minimum spanning tree)

```python

min_tree, weight_sum = g.prim(source) # return a new graph that represents the minimum spanning tree from g graph
                                      # and returns it's weight sum
                                      
```




