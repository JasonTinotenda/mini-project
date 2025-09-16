# Node class represents each element in the list
class Node:
    def __init__(self, data):
        self.data = data      # Value stored in the node
        self.next = None      # Pointer to the next node

# LinkedList class manages the list
class LinkedList:
    def __init__(self):
        self.head = None      # Start of the list

    # Add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Print all elements in the list
    def print_list(self):
        current = self.head
        while current:
           # print(current.data, end=" -> ")
           print(current.data)
           current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append (99)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None

 