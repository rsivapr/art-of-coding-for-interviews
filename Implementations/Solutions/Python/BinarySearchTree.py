class Node:
    def __init__(self, key):
        self.key = key
        self.left = False
        self.right = False

def find(key, node):
    if node == False or node.key == key:
        return node
    elif key < node.key:
        return find(key, node.left)
    else:
        return find(key, node.right)

def insert(key, node):
    if key < node.key:
        if node.left:
            insert(key, node.left)
        else:
            node.left = Node()
    if key > node.key:
        if node.right:
            insert(key, node.right)
        else:
            node.right = Node()