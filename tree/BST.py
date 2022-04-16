from xmlrpc.client import Boolean


class BinaryTreeNode:
	def __init__(self, data:any, left=None,  right=None) -> None:
		self.data:any = data
		self.left:BinaryTreeNode = left
		self.right:BinaryTreeNode = right

class BST:
	def __init__(self, root=None) -> None:
		if root:
			self.root = root
			self.len = 1
			self.depth = 1
		else:
			self.root = BinaryTreeNode(None)
			self.len = 0
			self.depth = 0

	def insert(self, node, child) -> None:
		if node.data == child.data:
			return

		if node.data < child.data:
			if node.right is None:
				node.right = child
			else:
				self.insert(node.right, child)
		
		elif node.data > child.data:
			if node.left is None:
				node.left = child
			else:
				self.insert(node.left, child)

		self.len += 1
		


	def search(self, node, data) -> None:
		# root node를 안넣으면 어떻게 되지?
		if node is None:
			return None
		
		if node.data == data:
			return node
		if node.data > data:
			return self.search(node.left, data)
		if node.data < data:
			return self.search(node.right, data)
	

	def search_min_node(self, node):
		if node is None:
			return None

		if node.left is None:
			return node
		else:
			return self.search_min_node(node.left)


	def remove(self, node, parent, target_data):
		removed = None
		
		if node is None:
			return None

		if (node.data > target_data):
			removed = self.remove(node.left, node, target_data)
		elif (node.data < target_data):
			removed = self.remove(node.right, node, target_data)
		else:
			removed = node
		
			if not node.left  and not node.right :
				if parent.left == node:
					parent.left = None
				else:
					parent.right = None

			else:
				if node.left and node.right:
					min_node = self.search_min_node(node.right)
					removed = self.remove(node, None, min_node.data)
					node.data = min_node.data
				else:
					temp = None
					if node.left:
						temp = node.left
					else:
						temp = node.right
					
					if parent.left == node:
						parent.left = temp
					else:
						parent.right = temp
		
		self.len -= 1

		return removed



	def print(self, node):
		if node is None:
			return

		self.print(node.left)

		print(f"[ {node.data} ]")

		self.print(node.right)

	def to_list(self, node, result):
		if node is None:
			return
		
		self.to_list(node.left, result)
		result.append(node.data)
		self.to_list(node.right, result)

		return result
		



def main():
	root = BinaryTreeNode(50)
	bs_tree = BST(root=root)
	data_size = 5
	for i in range(1, data_size):
		bs_tree.insert(root, BinaryTreeNode(50 - 10 * i))
		bs_tree.insert(root, BinaryTreeNode(50 - 10 * i + 1))
		bs_tree.insert(root, BinaryTreeNode(50 - 10 * i - 1))
		bs_tree.insert(root, BinaryTreeNode(50 + 10 * i))
		bs_tree.insert(root, BinaryTreeNode(50 + 10 * i + 1))
		bs_tree.insert(root, BinaryTreeNode(50 + 10 * i - 1))

	print(f" * * * initial tree * * * ")

	result = bs_tree.to_list(root, [])
	print(result)
	print(40 in result)

	removed = bs_tree.remove(root, None, 40)
	print(f"removed is {removed.data}")
	print(f" * * * after remove tree * * * ")

	result = bs_tree.to_list(root, [])
	print(result)
	print(40 not in result)





if __name__ == "__main__":
	main()




