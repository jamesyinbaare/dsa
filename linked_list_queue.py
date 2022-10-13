from pkg_resources import cleanup_resources


class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next  = None
        self.prev = None
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        node = Node(data)
        if self.head == None and self.tail == None:
            self.head =  self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
        self.count += 1

    def dequeue(self):
        if self.head == None:
            print("Queue empty")
        else:
            data = self.head.data
            if self.head.next == None:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.count -=1

            return data


words = Queue()
words.enqueue("eggs")
words.enqueue("ham")
words.enqueue("spam")


current = words.head

while current:
    print(words.dequeue())

    current = current.next


words.dequeue()