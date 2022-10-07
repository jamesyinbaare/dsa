
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        return f"({self.__class__.__name__} data={self.data} next={self.next})"

class CircularList:
    def __init__(self) -> None:
        self.tail = None
        self.head = None
        self.size = 0


    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        else:
            self.head = node
            self.tail = node
            self.tail.next = self.tail
        self.size +=1


    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.head
        prev = self.head
        flag = False

        while prev == current or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                    #flag = True
                elif current == self.tail:
                    self.tail = prev
                    prev.next = self.head
                    #flag = True
                else:
                    prev.next = current.next
                flag = True

            prev = current
            current = current.next
        if flag is False:
            print("Item not present in the list")

words = CircularList()
words.append('eggs')
words.append('ham')
words.append('spam')
words.append('foo')
words.append('bar')

print("Let us try to delete something that isn't in the list.")
words.delete('socks')
counter = 0
for item in words.iter():
    print(item)
    counter += 1
    if counter > 4:
        break

print("Let us delete something that is there.")
words.delete('foo')
counter = 0
for item in words.iter():
    print(item)
    counter += 1
    if counter > 3:
        break