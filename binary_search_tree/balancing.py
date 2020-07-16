import os
import sys
sys.path.append(f'{os.getcwd()}/singly_linked_list')
sys.path.append(f'{os.getcwd()}/binary_search_tree')
from singly_linked_list import LinkedList, Node
from binary_search_tree import BSTNode

my_list = LinkedList()
for i in range(20):
    my_list.add_to_tail(i + 1)


# counter = 0
# current = my_list.head

# while current.next_node is not None:
#     counter += 1
#     current = current.next_node

# half = int(counter / 2)

# counter = 0
# current = my_list.head
# prev = None
# while counter != half:
#     counter += 1
#     prev = current
#     current = current.next_node

# # current is our middle point
# next_node = current.next_node
# print(f"{current.value}")
# my_bst = BSTNode(current.value)

my_bst = None

def find_middle(start_ptr, end_ptr, bst):
    counter = 0
    current = start_ptr
    prev = None
    while current is not end_ptr:
        counter += 1
        prev = current
        current = current.next_node
    half = int(counter / 2)

    counter = 0
    current = start_ptr
    prev = None
    while counter != half:
        counter += 1
        prev = current
        current = current.next_node

    if bst is None:
        bst = BSTNode(current.value)
    else:
        bst.insert(current.value)

    left_start = start_ptr
    left_end = prev
    right_start = current.next_node
    right_end = end_ptr

    bst = find_middle(left_start, current, bst)
    bst = find_middle(current, right_end, bst)
    return bst
    # return find_middle()


my_bst = find_middle(my_list.head, my_list.tail, my_bst)
print(f"{my_bst.value}")