class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)

def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)

def postorder(root_node):
    current = root_node
    if current is None:
        return
    
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)

n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child =n2
n1.right_child =n3
n2.left_child = n4

print("=== Inorder Traversal ===")
inorder(n1)

print("=== Preoder Traversal ===")
preorder(n1)

print("=== Posteoder Traversal ===")
postorder(n1)