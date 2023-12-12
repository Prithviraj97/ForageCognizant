import sys

# Node class 
class Node:
    def __init__(self, data):
        self.data = data  
        self.left = None
        self.right = None
        self.color = 1 

# RB Tree  
class RBTree():
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = 0
        self.root = self.nil

    # Insert new node
    def insert(self, key):
        new_node = Node(key)  
        new_node.left = self.nil
        new_node.right = self.nil
        self._insert_helper(self.root, new_node)

    # Search for value      
    def search(self, key):
        return self._search_helper(self.root, key)

    # Insert logic  
    def _insert_helper(self, root, new_node):
        if root == self.nil:
            self.root = new_node  
            new_node.color = 0 
            return
        # Insert code 

    # Search logic
    def _search_helper(self, root, key):
        if root == self.nil or root.data == key:
            return root.data == key  
        elif key < root.data:
            return self._search_helper(root.left, key)
        else:
            return self._search_helper(root.right, key)
        

    def isRed(node):
        if node == Node.nil:
            return False
        return node.color == 1
    
T = RBTree()
T.insert(15)
print("Searching for 15 : ", T.search(15))