"""
Author: Partha Sen
"""
class HashEntry:
	def __init__(self, key, data):
		self.key = key
		self.value = data
		self.nxt = None
		
entry = HashEntry(3, "Partha")
print(str(entry.key) + ", " + entry.value)

class HashTable:
	def __init__(self):
		self.slots = 10
		self.size = 0
		self.bucket = [None] * self.slots
		self.threshold = 0.6
		
	def get_size(self):
		return self.size
		
	def is_empty(self):
		return self.get_size() == 0
		
	def get_index(self, key):
		hash_code = hash(key)
		index = hash_code % self.slots
		return index
	
	def resize(self):
		new_slots = self.slots * 2
		new_bucket = [None] * new_slots
		
		for i in range(0, len(self.bucket)):
			head = self.bucket[i]
			while head:
				new_index = hash(head.key) % new_slots
				if new_bucket[new_index] is None:
					new_bucket[new_index] = HashEntry(head.key, head.value)
				else:
					node = new_bucket[new_index]
					while node:
						if node.key is head.key:
							node.value = head.value
							node = None
						elif node.nxt is None:
							node.nxt = HashEntry(head.key, head.value)
							node = None
						else:
							node = node.nxt
			head = head.nxt
		self.bucket = new_bucket
		self.slots = new_slots
		
	def insert(self, key, value):
		b_index = self.get_index(key)
		if self.bucket[b_index] is None:
			self.bucket[b_index] = HashEntry(key, value)
			print(key, "-", value, "inserted at index:", b_index)
			self.size += 1
		else:
			head = self.bucket[b_index]
			while head:
				if head.key == key:
					head.value = value
					break
				elif head.nxt is None:
					head.nxt = HashEntry(key, value)
					print(key, "-", value, "inserted at index:", b_index)
					self.size += 1
					break
				head = head.nxt
		load_factor = float(self.size) / float(self.slots)
		if load_factor >= self.threshold:
			self.resize()
			
	def search(self, key):
		b_index = self.get_index(key)
		head = self.bucket[b_index]
		while head:
			if head.key == key:
				return head.value
			head = head.nxt
		return None
		
	def delete(self, key):
		b_index = self.get_index(key)
		head = self.bucket[b_index]
		
		if head.key == key:
			self.bucket[b_index] = head.nxt
			print(key, "-", head.value, "deleted")
			self.size -= 1
			return self
		
		prev = None
		while head is not None:
			if head.key == key:
				prev.nxt = head.nxt
				print(key, "-", head.value, "deleted")
				self.size -= 1
				return 
			prev = head
			head = head.nxt
			
		print("Key not found")
		return
		
ht = HashTable()
print(ht.is_empty())
ht.insert("This", 1)
ht.insert("is", 2)
ht.insert("a", 3)
ht.insert("Test", 4)
ht.insert("Driver", 5)
print("Table Size:" + str(ht.get_size()))
print("The value for 'is' key:" + str(ht.search("is")))
ht.delete("is")
ht.delete("a")
print("Table Size:" + str(ht.get_size()))
	
