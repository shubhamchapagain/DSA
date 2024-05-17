class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return
    
    current = head
    seen = set()
    seen.add(current.data)
    while current.next is not None:
        if current.next.data in seen:
            current.next = current.next.next  # Remove duplicate
        else:
            seen.add(current.next.data)
            current = current.next

# Helper function to print the list
def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)

print("Original list:")
print_list(head)
remove_duplicates(head)
print("List after removing duplicates:")
print_list(head)
