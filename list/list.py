

class Node:
	def __init__(self, data:any, prev=None,  next=None) -> None:
		self.data:any = data
		self.prev:Node = prev
		self.next:Node = next

class DoublyLinkedList:
	def __init__(self, data:any=None) -> None:
		if data is None:
			self.head:Node = None
			self.len:int = 0
		else:
			self.head:Node = Node(data)
			self.len:int = 1
		self.tail:Node = self.head
	
	def describe(self) -> None:
		node:Node = self.head
		print(f"이 리스트의 길이는 {self.len}입니다.")

		while node:
			print(node.data)
			node = node.next
	
	def push(self, data) -> None:
		if self.head == None:
			self.head = Node(data)
			self.tail = self.head
		
		else:
			new_node = Node(data)
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node
		self.len += 1
		

	def pop(self) -> Node:
		to_pop = self.tail.prev.next
		to_tail = self.tail.prev
		self.tail.prev.next = None
		self.tail = to_tail
		self.len -= 1
		return to_pop
	
	def find_by_index(self, index:int) -> Node | None:
		node:Node = self.head
		if self.len <= index + 1:
			return ErrorCase("index out of range", "그런 데이터는 없습니다.").says()
		if self.len // 2 > index:
			for _ in range(index):
				node = node.next
		else:
			node = self.tail
			for _ in range(index):
				node = node.prev
		return node

	def to_array(self) -> Node:
		node = self.head
		result = []
		while node:
			result.append(node.data)
			node = node.next
		return result

	def insert(self, node:Node, data:any) -> None:
		if node == None:
			return ErrorCase("no data", "node를 넣어주세요").says()
		new_node = Node(data)

		if node == self.head:
			new_node.next = node
			node.prev = new_node

		else:
			if node.prev is None:
				return ErrorCase("wrong data", "잘못된 데이터").says()
			node.prev.next = new_node
			node.prev = new_node
			new_node.next = node
			new_node.prev = node.prev
		self.len += 1
	
	def update(self, to_update_node:Node, data:any) -> None:
		to_update_node.data = data
	
	def delete(self, to_delete_node) -> None:
		to_delete_node.prev.next = to_delete_node.next
		to_delete_node.next.prev = to_delete_node.prev
		to_delete_node.prev = None
		to_delete_node.next = None
		to_delete_node.data = None
		to_delete_node = None
		self.len -= 1

class ErrorCase:
	def __init__(self, case: str, description: str) -> None:
		self.case:str = case
		self.description:str = description
	
	def says(self) -> None:
		print(f"[{self.case}] {self.description}")

def test(assert_data:bool, description:str="결과가 잘 나왔는가 ?") -> None:
	print(f"[TEST] {description} {assert_data} ")

def pretty_print(to_print:str) -> None:
	print(f" * * * {to_print} * * * ")

def main():
	print("hello world")

	pretty_print("나와라 민욱햄")
	new_list = DoublyLinkedList()
	new_list.push("황민욱")
	new_list.describe()
	print()

	pretty_print("나와라 임채욱")
	new_list.push("임채욱")
	new_list.describe()
	print()

	pretty_print("임채욱 사라지기")
	popped = new_list.pop()
	new_list.describe()
	print(f"popped? : {popped.data}")
	print()


	pretty_print("여러명 넣기")
	names = ["박성민", "윤수진", "임채욱", "강민지"]
	expected = ["황민욱"]


	for name in names:
		new_list.push(name)
		expected.append(name)
	new_list.describe()
	test(len(expected) == new_list.len)
	print()

	pretty_print("세번째 사람 나와라")
	third_person = new_list.find_by_index(2)
	print(f"세번째 사람은 ? : {third_person.data}")
	test(third_person.data == expected[2])
	print()

	pretty_print("100번째 사람 나와라")
	a_hundred_person = new_list.find_by_index(99)
	print()

	pretty_print("리스트 내놔")
	print(new_list.to_array())
	print()

	pretty_print("세번째 사람 나가고 보리 들어와")
	new_list.update(third_person, "보리")
	new_list.describe()
	print()

	pretty_print("보리 나가")
	new_list.delete(third_person)
	new_list.describe()
	print()

	pretty_print("세번째에 윤수진 넣어")
	third_person = new_list.find_by_index(2)
	print(f"third_person : {third_person.data}")
	new_list.insert(third_person, "윤수진")
	new_list.describe()
	print()

if __name__ == "__main__":
	main()





