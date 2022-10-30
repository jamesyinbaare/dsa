class Queue:
    def __init__(self) -> None:
        self.Stack1 = []
        self.Stack2 = []
    
    def enqueue(self, data):
        self.Stack1.append(data)

    def dequeue(self):
        if not self.Stack1:
            print("Queue empty")
        else:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
            data = self.Stack2.pop()

            while self.Stack2:
                self.Stack1.append(self.Stack2.pop())
            
            return data


queue = Queue()
queue.enqueue(23)
queue.enqueue(13)
queue.enqueue(11)
print(queue.Stack1)
queue.dequeue()
print(queue.Stack1)