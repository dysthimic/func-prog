class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def print(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next


def head_swap_pairs(head):
    if not head or not head.next:
        return head
    else:
        next_node = head.next
        head.next = head_swap_pairs(next_node.next)
        next_node.next = head
        return next_node


def tail_swap_pairs(head, prev=None):
    if not head or not head.next:
        if prev:
            return prev.next
        else:
            return head
    else:
        next_node = head.next
        head.next = next_node.next
        next_node.next = head
        if prev:
            prev.next = next_node
        tail_swap_pairs(head.next, head)
        return next_node


llist = LinkedList()

for i in range(4):
    llist.insert(i)

# Список
print('Список:')
llist.print()

print('Головна рекурсія:')
llist.head = head_swap_pairs(llist.head)
llist.print()

print('Хвостова рекурсія(приміняється до списку, який був результатом головної рекурсії):')
llist.head = tail_swap_pairs(llist.head)
llist.print()
