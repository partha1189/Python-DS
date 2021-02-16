class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next
		
	def append(self, data):
		#append to the end of list
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node
		
	def prepend(self, data):
		#prepend to the start(head) of list
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		
	def insert_after_node(self, prev_node, data):
		#insert after a given Node
		if not prev_node:
			print("Previous node does not exist.")
			return
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node
		
	def delete_node(self, key):
			#delete node which is not head and which is not head(DELETE BY VALUE)
			cur_node = self.head
			
			if cur_node and cur_node.data == key:
				self.head = cur_node.next
				cur_node = None
				return
			prev = None
			while cur_node and cur_node.data != key:
				prev = cur_node
				cur_node = cur_node.next
				
			if cur_node is None:
				return 
				
			prev.next = cur_node.next
			cur_node = None
			
	def delete_node_at_pos(self, pos):
		#delete node at position
		if self.head:
			cur_node = self.head
			if pos == 0:
				self.head = cur_node.next
				cur_node = None
				return 
			
			prev = None
			count = 0
			while cur_node and count != pos:
				prev = cur_node
				cur_node = cur_node.next
				count += 1
				
			if cur_node is None:
				return 
				
			prev.next = cur_node.next
			cur_node = None
		
	def len_iterative(self):
		count = 0
		cur_node = self.head
		while cur_node:
			count +=1
			cur_node = cur_node.next
		return count
		
	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)
		
	def swap_nodes(self, key_1, key_2):
		#swap two nodes with provided keys
		if key_1 == key_2:
			return 
		
		prev_1 = None
		curr_1 = self.head
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next
			
		prev_2 = None
		curr_2 = self.head
		
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2
			curr_2 = curr_2.next
			
		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2
			
		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1
			
		curr_1.next, curr_2.next = curr_2.next, curr_1.next
		
	def reverse_iterative(self):
		#reverse the list
		prev = None
		cur = self.head
		while cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
		self.head = prev
		
	def reverse_recursive(self):
		#helper function below
		def _reverse_recursive(cur, prev):
			if not cur:
				return prev
			
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			return _reverse_recursive(cur, prev)
			
		self.head = _reverse_recursive(cur=self.head, prev=None)
		
	def merge_sorted(self, llist):
		#merge two sorted lists
		p = self.head
		q = llist.head
		s = None
		
		if not p:
			return q
		if not q:
			return p
		
		if p and q:
			if p.data <= q.data:
				s = p
				p = s.next
			else:
				s = q
				q = s.next
			new_head = s
		while p and q:
			if p.data <= q.data:
				s.next = p
				s = p
				p = s.next
			else:
				s.next = q
				s = q
				q = s.next
		if not p:
			s.next = q
		if not q:
			s.next = p
			
		self.head = new_head
		return self.head
		
	def remove_duplicates(self):
		#remove duplicates in list
		cur = self.head
		prev = None
		dup_values = dict()
		
		while cur:
			if cur.data in dup_values:
				#remove node
				prev.next = cur.next
				cur = None
			else:
				dup_values[cur.data] = 1
				prev = cur
			cur = prev.next

	def print_nth_from_last(self, n):
		total_len = self.len_iterative()
		
		cur = self.head
		while cur:
			if total_len == n:
				print(cur.data)
				return cur.data
			total_len -= 1
			cur = cur.next
		if cur is None:
			return
			
	def rotate(self, k):
		#rotate list around a pivot k
		if self.head and self.head.next:
			p = self.head
			q = self.head
			prev = None
			count = 0
			
			while p and count<k:
				prev = p
				p = p.next
				q = q.next
				count += 1
			p = prev
			
			while q:
				prev = q
				q = q.next
				
			q = prev
			
			q.next = self.head
			self.head = p.next
			p.next = 	None
												
	def is_palindrome(self, method):
		#find if palindrom using 3 methods
		if method == 1:
			return self.is_palindrome_1()
		elif method == 2:
			return self.is_palindrome_2()
		elif method == 3:
			return self.is_palindrome_3()
	
	def is_palindrome_1(self):
		#using string
		s = ""
		p = self.head
		while p:
			s += p.data
			p = p.next
		return s == s[::-1]
		
	def is_palindrome_2(self):
		#using stack
		p = self.head
		s = []
		while p:
			s.append(p.data)
			p = p.next
		p = self.head
		
		while p:
			data = s.pop()
			if p.data != data:
				return false
			p = p.next
		return True
		
	def is_palindrome_3(self):
		#using two pointers
		pass
		
	def move_tail_to_head(self):
		if self.head and self.head.next:
			p = self.head
			prev = None
			while p.next:
				prev = p
				p = p.next
			print(prev.data)
			prev.next = None
			p.next = self.head
			self.head = p
			
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")
llist.append("E")

llist.insert_after_node(llist.head.next, "F")
llist.print_list()

llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")

llist.print_list()

llist.delete_node("B")
llist.delete_node("E")
llist.delete_node_at_pos(3)
print("*********")

llist.print_list()
print(llist.len_iterative())
print(llist.len_recursive(llist.head))

llist.reverse_iterative()
llist.print_list()

llist.reverse_recursive()
llist.print_list()
