import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class NodeManager:
    def __init__(self, node=None):
        self.head = node

    def print(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

head = Node(1)
prev = head
if n > 1:
    for number in range(2, n+1):
        node = Node(number)
        if prev:
            prev.next = node
        prev = node
    node.next = head

    node_manager = NodeManager(head)
    count = 0
    while count < n:
        if count < 1:
            print('<', end='')
        else:
            print(', ', end='')
        for _ in range(k - 1):
            node = node.next
        prev = node
        node = node.next
        print(node.data, end='')
        node.data = None
        prev.next = node.next
        count += 1
    print('>')
else:
    print("<1>")






