import sys
sys.path.append("/Users/scott/dev/lambda/CS/Data-Structures/singly_linked_list")
from singly_linked_list import LinkedList, Node

def reverse_ll(ll):
    current = ll.head
    prev = None

    while current is not None:

        next_node = current.next_node

        current.next_node = prev

        prev = current

        current = next_node

    ll.head, ll.tail = ll.tail, ll.head
    # return ll
    

my_list = LinkedList()
my_list.add_to_tail(1)
my_list.add_to_tail(2)
my_list.add_to_tail(3)

my_current = my_list.head

while my_current is not None:
    print(f"{my_current.get_value()}")
    my_current = my_current.next_node


reverse_ll(my_list)

my_current = my_list.head

while my_current is not None:
    print(f"{my_current.get_value()}")
    my_current = my_current.next_node




