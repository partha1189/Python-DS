"""
Author: Partha Sen 
"""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
		
		
class DoublyLinkedList():
	def __init__(self):
		self.head = None
		
	def append(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			cur = self.head
			while cur.next:
				cur = cur.next
			cur.next = new_node
			new_node.prev = cur
			
	def print_list(self):
		cur = self.head
		while cur:
			print(cur.data)
			cur = cur.next
			
	def prepend(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			self.head.prev = new_node
			new_node.next = self.head
			self.head = new_node
			
	def add_after_node(self, key, data):
		#add node after node
		cur = self.head
		while cur:
			if cur.next is None and cur.data == key:
				self.append(data)
				return 
			elif cur.data == key:
				new_node = Node(data)
				nxt = cur.next
				cur.next = new_node
				new_node.next = nxt
				new_node.prev = cur
				nxt.prev = new_node
				return 
			cur = cur.next
			
	def add_before_node(self, key, data):
		#add node before node
		cur = self.head
		while cur:
			if cur.prev is None and cur.data == key:
				self.prepend(data)
				return 
			elif cur.data == key:
				new_node = Node(data)
				prev = cur.prev
				prev.next = new_node
				new_node.next = cur
				cur.prev = new_node
				new_node.prev = prev
				return 
			cur = cur.next
			
	def delete(self, key):
		#delete node has 4 cases
		cur = self.head
		while cur:
			if cur.data == key and cur == self.head:
				# Case 1 Deleting only node present
				if not cur.next:
					cur = None
					self.head = None
					return 
				#Case 2 Deleting Head Node	
				else:
					nxt = cur.next
					cur.next = None
					nxt.prev = None
					cur =	None
					self.head = nxt
					return
					
			elif cur.data == key:
				#Case 3 Delete Node other than Head where cur.next is not None
				if cur.next:
					nxt = cur.next
					prev = cur.prev
					prev.next = nxt
					nxt.prev = prev
					cur.next = None
					cur.prev = None
					cur = None
					return 
					
				#Case 4 Delete node other than head where cur.next is None
				else:
					prev = cur.prev
					cur.prev = None
					prev.next = None
					cur = None
					return 
			cur = cur.next
			
	def reverse(self):
		tmp = None
		cur = self.head
		while cur:
			tmp = cur.prev
			cur.prev = cur.next
			cur.next = tmp
			cur = cur.prev
		if tmp:
			self.head = tmp.prev
				
				
				
			
