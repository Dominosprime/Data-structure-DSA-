# 1821322

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def insert(self, data):
        """Inserts a new node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse_and_find_middle(self):
        """Reverses the linked list and finds the middle element in a single traversal."""
        prev = None
        slow = fast = self.head
        
        while fast and fast.next:
            fast = fast.next.next  # Move fast pointer two steps ahead
            temp = slow.next  # Save next node
            slow.next = prev  # Reverse current node
            prev = slow  # Move prev to current node
            slow = temp  # Move slow one step ahead

        # Reverse the remaining part if needed
        if slow:
            temp = slow.next
            slow.next = prev
            prev = slow

        self.head = prev  # Update head to new reversed list
        
        middle_element = slow.data if slow else None
        return middle_element

    def display(self):
        """Displays the linked list."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example Usage
ll = LinkedList()
elements = [1, 2, 3, 4, 5, 6, 7]  # Example list
for el in elements:
    ll.insert(el)

print("Original List:")
ll.display()

middle = ll.reverse_and_find_middle()

print("\nReversed List:")
ll.display()
print("\nMiddle Element:", middle)