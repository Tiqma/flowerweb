class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode("two")
head.next.next.next.next = ListNode(5)

def print_linked_list(node):
    while node:
        if node.value == "two":
            node.value = "three"
        print(node.value)
        node = node.next

def print_last(node):
    while node.next:
        node = node.next
    print(node.value)

print_last(head)
