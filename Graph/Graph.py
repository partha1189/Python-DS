"""
Author: Partha Sen
"""
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from LinkedList import LinkedList

class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		
		self.array = []
		
		for i in range(vertices):
			temp = LinkedList()
			self.array.append(temp)
			
	def add_edge(self, source, destination):
		if (source < self.vertices and destination < self.vertices):
			self.array[source].prepend(destination)

	def print_graph(self):
		print(">>Adjacency List of Directed Graph<<")
		print
		for i in range(self.vertices):
			print("|", i, end=" | => ")
			temp = self.array[i].head
			while(temp is not None):
				print("[", temp.data, end=" ] -> ")
				temp = temp.next
			print("None")
			
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()

print(g.array[1].head.data)
