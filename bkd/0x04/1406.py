string = input()
count = int(input())

index = len(string)

class Cursor:
    def __init__(self, character=''):
        self.next = None
        self.prev = None
        self.data = character

class CursorManager:
    def __init__(self, string=''):
        self.head = None
        self.tail = None
        self.string = string
        self.index = len(string)
    
    def get_head_n_tail(self):
        prev = self.head
        for s in self.string:
            cursor = Cursor(s)
            if prev:
                prev.next = cursor
            else:
                self.head = cursor
            cursor.prev = prev
            prev = cursor
        return self.head, cursor

    def print(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def get_left(self, cursor):
        if cursor.prev:
            cursor = cursor.prev
            self.index -= 1
    
    def get_right(self, cursor):
        if cursor.next:
            cursor = cursor.next
            self.index += 1
    
    def erase(self, cursor):
        cursor.data = None
        cursor.prev.next = cursor.prev.next.next
        cursor.next.prev = cursor.next.prev.prev
        cursor.prev = None
        cursor.next = None
    
    def insert(self, cursor, key):
        new_cursor = Cursor(key)
        cursor.next.prev = new_cursor
        new_cursor.next = cursor.next
        cursor.next = new_cursor
        new_cursor.prev = cursor
        self.index += 1

cursorM = CursorManager(string)
cursorM.print()


cursor = None





 
print(string)


