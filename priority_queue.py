class Node:
    def __init__(self, info, priority) -> None:
        self.info = info
        self.priority = priority


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    def insert(self, node):
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            for x in range(0, len(self.queue)):
                if node.priority <= self.queue[x].priority:
                    if x == (len(self.queue) -1):
                        self.queue.insert(x+1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x,node)
                    return True
    def delete(self):
        x = self.queue.pop()
        print("Deleted data with the given priority-", x.info, x.priority)
        return x
    
    def show(self):
        for x in self.queue:
            print(str(x.info) + " - "+str(x.priority))

p = PriorityQueue()
p.insert(Node("Cat", 13))
p.insert(Node("Bat", 2))
p.insert(Node("Rat", 1))
p.insert(Node("Ant", 26))
p.insert(Node("Lion", 25))
p.show()
p.delete()
p.show()
p.delete()
p.show()
p.delete()
p.show()