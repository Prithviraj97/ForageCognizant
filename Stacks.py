class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def push(self, data):
    # Create a node with the data
    new_node = Node(data)
    if self.top:
      new_node.next = self.top
    # Set the created node to the top node
    self.top = new_node
    # Increase the size of the stack by one
    self.size += 1

  def pop(self):
    # Check if there is a top element
    if self.top is None:
      return None
    else:
      popped_node = self.top
      # Decrement the size of the stack
      self.size -= 1
      # Update the new value for the top node
      self.top = self.top.next
      popped_node.next = None
      return popped_node.data 


# Import the module to work with Python's LifoQueue
import queue
# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize=0)
# Add an element to the stack
my_book_stack.put("Don Quixote")
# Remove an element from the stack
my_book_stack.get()

#
def has_elements(self):
     """Check if the stack has elements"""
     return self.head != None

class PrinterTasks:
  def __init__(self):
    self.queue = Queue()
      
  def add_document(self, document):
    # Add the document to the queue
    self.queue.enqueue(document)
      
  def print_documents(self):
    # Iterate over the queue while it has elements
    while self.queue.has_elements():
      # Remove the document from the queue
      print("Printing", self.queue.dequeue())

#Runtime is O(1)
def enqueue(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node 
def dequeue(self):
    if self.head:
      current_node = self.head
      self.head = current_node.next
      current_node.next = None

      if self.head == None:
        self.tail = None

