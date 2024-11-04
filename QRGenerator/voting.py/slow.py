class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def has_cycle(head: ListNode) -> bool:
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next           # Move slow pointer by 1
        fast = fast.next.next      # Move fast pointer by 2

        if slow == fast:           # Cycle detected
            return True

    return False                  # No cycle detected
# Creating a linked list with a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle here

# Testing for a cycle
print(has_cycle(node1))  # Output: True

# Creating a linked list without a cycle
node5 = ListNode(5)
node6 = ListNode(6)
node5.next = node6

print(has_cycle(node5))  # Output: False
