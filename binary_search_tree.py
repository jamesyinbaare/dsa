from cmath import inf
import math

class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.root_node = None
    
    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return self.root_node
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return self.root_node
    
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                print("Item not found")
                return None
            elif current.data is data:
                print("Item found", data)
                return data
            elif current.data > data:
                current = current.left
            else:
                current = current.right

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        
        while current: #book used True
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        
        return (parent, current)

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        children_count = 0

        if node.left and node.right:
            children_count = 2
        elif (node.left is None) and (node.right is None):
            children_count = 0
        else:
            children_count = 1
        
        if children_count == 0:
            if parent:
                if parent.right == node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                self.root_node = None
            
        elif children_count == 1:
            next_node = None
            if node.left:
                next_node = node.left
            else:
                next_node = node.right
            
            if parent:
                if parent.left is node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right
            while leftmost_node.left:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left
            
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left == leftmost_node:
                parent_of_leftmost_node.left = leftmost_node.right
            else:
                parent_of_leftmost_node.right = leftmost_node.right


    def min(self):
        current = self.root_node
        if current is None:
            print("Tree is empty")
            return None
       
        while True:
            if current.left:
                current = current.left
            else:
                return current.data

    def max(self):
        current = self.root_node
        if current is None:
            print("Tree empty")
            return None

        while True:
            if current.right:
                current = current.right
            else:
                return current.data

    def longest_path(self, root):

        if root is None:
            return 0
        else:
            return root.data + max(self.longest_path(root.left), self.longest_path(root.right))
    
    def shortest_path(self, root):
        if root is None:
            return 0
        else:
            return root.data + min(self.shortest_path(root.left), self.shortest_path(root.right))

        

    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)
print("Longest Path, ", tree.longest_path(tree.root_node))
print("Shortest Path, ", tree.shortest_path(tree.root_node))

#tree.insert(1)
#tree.insert(6)
#tree.insert(100)
#tree.insert(-6)
#print("Min", tree.min())
#print("Max", tree.max())
#print("Root node,",  tree.root_node.data)
#
#tree.search(5)
#tree.remove(5)
#tree.search(5)
#print("Root node,",  tree.root_node.data)
#