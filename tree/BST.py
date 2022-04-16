from xmlrpc.client import Boolean


class Node:
	def __init__(self, data:any, left=None,  right=None) -> None:
		self.data:any = data
		self.left:Node = left
		self.right:Node = right

class BST:
	def __init__(self, root=None) -> None:
		self.root = root
		self.size = len(self.root)

	def insert(self, data) -> None:
		self.current = self.root

		while True:
			if data > self.current.data:
				if self.current.right:
					self.current = self.current.right
				else:
					self.current.right = Node(data)
					break
			else:
				if self.current.left:
					self.current = self.current.left
				else:
					self.current.left = Node(data)
					break
			
	def search(self, data) -> None:
		
		self.current = self.root

		while self.current:
			if self.current.data == data:
				return self.current
			elif self.current.data < data:
				self.current = self.current.right
			else:
				self.current = self.current.left
		return None
	
	def is_exist(self, data) -> Boolean:

		self.current = self.root

		while self.current:
			if self.current.data == data:
				return True
			elif self.current.data < data:
				self.current = self.current.right
			else:
				self.current = self.current.left
		return False

	def remove(self, data):
		pass

	def print(self):
		pass





