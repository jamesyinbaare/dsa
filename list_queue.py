
from multiprocessing import set_forkserver_preload
from time import sleep


class ListQueue:
    def __init__(self) -> None:
        self.items = []
        self.front = self.rear = 0
        self.size = 3

    def enqueue(self, data):
        if self.size == self.rear:
            print("\n Queue is full")
        else:
            self.items.append(data)
            self.rear +=1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            data = self.items.pop(0)
            self.rear -=1
            return data


q= ListQueue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.items)

print("Dequeuing")
data = q.dequeue()
print(data)
print(q.items)