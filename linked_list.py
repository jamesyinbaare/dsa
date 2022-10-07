


class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
    
    def append(self, data):
        node = Node(data)

        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size +=1

    def append_at_a_location(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1

        while current:
            if index == 1:
                node.next = current
                self.head = node
                self.size +=1
                return
            elif count == index:
                node.next = current
                prev.next = node
                self.size +=1
                return
            count +=1
            prev = current
            current = current.next
            if count < index:
                print("The lis has less number of elements")

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False
    
    #def size(self):
    #    count = 0
    #    current = self.head
    #    while current:
    #        count +=1
    #        current = current.next
    #    
    #    return count

    def delete_first_node(self):
        current  = self.head
        if self.head is None:
            print("No data element to delete")
        elif current == self.head:
            self.head = current.next
            self.size -=1

    def delete_last_node(self):
        current = self.head
        prev = self.head
        while current:
            if current.next is None:
                prev.next = current.next
                self.size -=1
            prev = current
            current = current.next
    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                
                self.size -=1
                return
            
            prev = current
            current = current.next

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0




words = SinglyLinkedList()
words.append("eggs")
words.append("ham")
words.append("spam")
words.delete_first_node()
words.delete("ham")

current = words.head
while current:
    print(current.data)
    current = current.next



print(words.search('sspam'))
print(words.search('spam'))

print(f"count: {words.size}")