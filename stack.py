from hashlib import new
from locale import currency


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    
    def push(self, data):
        node = Node(data=data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size +=1

    def pop(self):
        
        if self.top:
            self.size -=1
            data = self.top.data
            self.top = self.top.next
            return data
        else:
            return None
            
    def peek(self):
        if self.top:
            return self.top.data
        else:
            print("stack is empty")
            return None

words = Stack()
words.push("egg")
words.push("ham")
words.push("spam")

current = words.top

while current:
    print(current.data)
    current = current.next

print("peeking .....",words.peek())
print("poping .....",words.pop())
print("peeking .....",words.peek())
print("poping .....",words.pop())
print("peeking .....",words.peek())
print("poping .....",words.pop())
print("peeking .....",words.peek())
print("poping .....",words.pop())

print("===After pop()===")
current = words.top
while current:
    print(current.data)
    current = current.next