class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

node_A = LinkedList(1)
node_B = LinkedList(2)
node_C = LinkedList(3)

node_A.next = node_B
node_B.next = node_C

def pop(head):
    current_node = head
    while current_node.__next:
        if current_node.__next == None:
            del current_node
            break
        else:
            current_node = current_node.__next

def listValues(head):
  values = []
  current_node = head
  while current_node.__next:
    values.append(current_node.value)
    current_node = current_node.__next
  return values

try:
    pop(node_A)
    print(listValues(node_A))
except NameError:
    pass

if __name__ == "__main__":
    # Write your solution here
    pass
