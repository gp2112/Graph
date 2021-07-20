
#
#	Min-Heap Implementation in Python
#		by Guilherme Paixão
#
#


def weight(root):
	if root is None:
		return -1
	return root.weight

class Node:

		def __init__(self, item):
			self.item = item
			self.weight = 0 # how many nodes down this node
			self.left = None
			self.right = None

		def __str__(self):
			return str(self.item)

		def heapfy_down(self, comp):
			if self.left is not None and comp(self.left.item, self.item):
				aux = self.item
				self.item = self.left.item
				self.left.item = aux
				self.left.heapfy_down(comp)

			if self.right is not None and comp(self.right.item, self.item):
				aux = self.item
				self.item = self.right.item
				self.right.item = aux
				self.right.heapfy_down(comp)

		def minheapfy(self, comp):
			if self.left is not None and comp(self.left.item, self.item):
				aux = self.item
				self.item = self.left.item
				self.left.item = aux

			elif self.right is not None and comp(self.right.item, self.item):
				aux = self.item
				self.item = self.right.item
				self.right.item = aux

		def extract_last(self):
			last = self.item

			if weight(self.left) > weight(self.right):
				if weight(self.left) == 0:
					last = self.left.item
					self.left = None
				else:
					last = self.left.extract_last()

			elif weight(self.right) == 0:
				last = self.right.item
				self.right = None

			else:
				last = self.right.extract_last()

			self.weight -= 1
			return last

		def insert(self, item, comp):
			if weight(self.left) < weight(self.right):
				if self.left is None:
					self.left = Node(item)
				else:
					self.left.insert(item, comp)

			else:
				if self.right is None:
					self.right = Node(item)
				else:
					self.right.insert(item, comp)

			self.weight += 1
			self.minheapfy(comp)

		def printall(self):
			print(f'Node: {self}\nWeight: {self.weight}\nLeft: {self.left}\nRight: {self.right}\n')

			if self.left is not None:
				self.left.printall()
			if self.right is not None:
				self.right.printall()

class MinHeap:

	def __init__(self, comp = lambda x, y: x < y):
		self.root = None
		self.comp = comp

	def __len__(self):
		if self.root is None:
			return 0
		return self.root.weight+1

	def print(self):
		print('root: ', end='')
		if self.root is not None:
			self.root.printall()
		else:
			print('None')

	def heapfy_down(self):
		self.root.heapfy_down(self.comp)

	def insert(self, item):
		if self.root is None:
			self.root = Node(item)
		else:
			self.root.insert(item, self.comp)

	def min_extract(self):
		if self.root is None:
			return None
		min_ = self.root.item
		if self.root.weight == 0:
			self.root=None
			return min_

		last = self.root.extract_last()
		self.root.item = last
		self.root.heapfy_down(self.comp)
		return min_


# comparing bin min heap with simple list
# python3 minheap.py [number_of_itens]
if __name__ == '__main__':
	import random, time, sys

	vals = [random.randint(0, 10000) for _ in range(int(sys.argv[1]))]

	heap = MinHeap(random.randint(0, 10000))
	#print(vals)
	for val in vals:
		#print('inserting ', val)
		heap.insert(val)

	print('=== BIN MIN HEAP ===')

	t0 = time.time()
	heap.insert(random.randint(0, 10000))
	print(f'\nInsertion time: {time.time() - t0} seconds')

	#heap.print()

	t0 = time.time()
	heap.min_extract()
	print(f'\nMin Extraction time: {time.time() - t0} seconds')

	print('===================')


	print('=== SIMPLE LIST ===')

	t0 = time.time()
	vals.insert(len(vals)//2, random.randint(0, 10000))
	print(f'\nInsertion time: {time.time() - t0} seconds')

	#heap.print()

	t0 = time.time()
	vals.remove(vals[len(vals)//2])
	print(f'\nMin Extraction time: {time.time() - t0} seconds')

	print('===================')
	