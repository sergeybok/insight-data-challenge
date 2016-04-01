import time
from datetime import datetime, timedelta

# Node class
class Node:
	def __init__(self,hashtag):
		self.tag = hashtag
		self.num_edges = 0

	def add_edge(self):
		self.num_edges += 1
	def sub_edge(self):
		self.num_edges -= 1
	def get_num_edges(self):
		return self.num_edges
	def print_node(self):
		print(self.tag, self.num_edges)

# Edge class
class Edge:
	def __init__(self,n1,n2):
		self.node1 = n1
		self.node2 = n2
		self.timestamp = datetime.min

	def update_time(self,t):
		if (t > self.timestamp):
			self.timestamp = t
	def get_max_time(self):
		return self.timestamp
	def has_tag(self,hashtag):
		return (hashtag == self.node1.tag or hashtag == self.node2.tag)
	def get_node(self,hashtag):
		if (hashtag == self.node1.tag):
			return self.node1
		if (hashtag == self.node2.tag):
			return self.node2
		return None
	def print_edge(self):
		print ((self.node1.tag, self.node2.tag))


# Graph Utility class
#   Creates a graph of tags
#   Has methods for adding new connected tags
#      and updating graph based on time
class Graph_Util:
	def __init__(self):
		self.nodes = []
		self.edges = []
		self.max_time = datetime.min

	def add_tweet(self, tags, timestamp):
		if (timestamp > self.max_time):
			# Last tweet is later than max time, need to update graph
			self.update_graph(timestamp)

		elif (self.max_time - timestamp) >= timedelta(seconds = 60):
			# Last tweet is 60 secs older than max time, disregard it
			return
			
		tag1 = ""
		tag2 = ""
		for i in range(0,len(tags)):
			for j in range(i+1,len(tags)):
				tag1 = tags[i]
				tag2 = tags[j]
				n1 = None
				n2 = None

				b = True
				for e in self.edges:
					if (e.has_tag(tag1)):
						n1 = e.get_node(tag1)
					if (e.has_tag(tag2)):
						n2 = e.get_node(tag2)
					if (e.has_tag(tag1) and e.has_tag(tag2)):
						e.update_time(timestamp)
						b = False
						break
				if (b):
					if (n1 == None):
						n1 = Node(tag1)
						self.nodes.append(n1)
					if (n2 == None):
						n2 = Node(tag2)
						self.nodes.append(n2)

					e = Edge(n1, n2)
					e.update_time(timestamp)
					n1.add_edge()
					n2.add_edge()
					self.edges.append(e)

	def delete_node(self,n):
		if n in self.nodes:
			self.nodes.remove(n)
			return True
		# Shouldn't happen
		return False

	def delete_edge(self,e):
		n1 = e.node1
		n2 = e.node2
		n1.sub_edge()
		n2.sub_edge()
		if (n1.get_num_edges() < 1):
			self.delete_node(n1)
		if (n2.get_num_edges() < 1):
			self.delete_node(n2)
		if e in self.edges:
			self.edges.remove(e)
			return True
		# Shouldn't happen
		return False

	def update_graph(self,t):
		if (t>self.max_time):
			self.max_time = t
		else:
			# No need to update graph, max time > last tweet's time
			return
		to_delete = []
		for e in self.edges:
			if (self.max_time - e.get_max_time()) >= timedelta(seconds = 60):
				to_delete.append(e)
		for e in to_delete:
			self.delete_edge(e)

	def get_avg_degree(self):
		if (len(self.nodes) == 0):
			return 0
		return ((len(self.edges)*2) / len(self.nodes))








