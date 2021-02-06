class Node():
	
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node
		
	def set_next_node(self, next_node):
		self.next_node = next_node
		
	def get_next_node(self):
		return self.next_node
		
	def get_value(self):
		return self.value
		
		
bob = Node("Bob")
ricky = Node("Ricky")
john = Node("John")

print(bob.get_value())

bob.set_next_node(john)
john.set_next_node(ricky)

ricky_val = john.get_next_node().get_value()

print(ricky_val)
