#create CreateTree() class.
class TreeNode:  
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left_child = left
    self.right_child= right

class CreateTree:
  def insert(self, root, value):
    if root is None or value < root.data:
      temp = TreeNode(value)
      root = temp
    elif value > root.data:
        if root.right_child is None:
             root.right_child = TreeNode(value)
        else:

            self.insert(root.right_child, value)
    return root



class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = TreeNode(data)
    # Check if the BST is empty
    if self.root == None:
      self.root = new_node
      return
    else:
      current_node = self.root
      while True:
        # Check if the data to insert is smaller than the current node's data
        if data < current_node.data:
          if current_node.left_child == None:
            current_node.left_child = new_node
            return 
          else:
            current_node = current_node.left_child
        # Check if the data to insert is greater than the current node's data
        elif data > current_node.data:
          if current_node.right_child == None:
            current_node.right_child = new_node
            return
          else:
            current_node = current_node.right_child

bst = CreateTree()
bst.insert("Pride and Prejudice")
print(search(bst, "Pride and Prejudice"))


class BinarySearchTree:
  def __init__(self):
    self.root = None

#We only check the left_child of the tree coz left side of the root node only contains value smaller than the root itself.
  def find_min(self):
    # Set current_node as the root
    current_node = self.root
    # Iterate over the nodes of the appropriate subtree
    while current_node.left_child:
      # Update current_node
      current_node = current_node.left_child
    return current_node.data
  
bst = CreateTree()
print(bst.find_min())

#Another BST class.
class BinarySearchTree:
  def __init__(self):
    self.root = None

  def in_order(self, current_node):
    # Check if current_node exists
    if current_node:
      # Call recursively with the appropriate half of the tree
      self.in_order(current_node.left_child)
      # Print the value of the current_node
      print(current_node.data)
      # Call recursively with the appropriate half of the tree
      self.in_order(current_node.right_child)
  
bst = CreateTree()
bst.in_order(bst.root)


import queue
#Expression tree are a kind of Binary Tree that represents arithmetic expressions.
class ExpressionTree:
  def __init__(self):
    self.root = None

  def pre_order(self, current_node):
    # Check if current_node exists
    if current_node:
      # Print the value of the current_node
      print(current_node.data)
      # Call pre_order recursively on the appropriate half of the tree
      self.pre_order(current_node.left_child)
      self.pre_order(current_node.right_child)
          
et = CreateExpressionTree()
et.pre_order(et.root)