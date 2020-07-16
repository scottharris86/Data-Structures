import sys
sys.path.append("/Users/scott/dev/lambda/CS/Data-Structures/singly_linked_list")
from singly_linked_list import LinkedList, Node

def reverse_ll(ll):
    current = ll.head # 1, 2, 3
    if current != None:
        print(f"current is: {current.get_value()}")
    else:
        print("current is None")
    prev = None # -- 1, 2

    while current is not None:

        next_node = current.next_node  # next_node = 2 --- 3, None

        if next_node != None:
            print(f"next_node is: {next_node.get_value()}")
        else:
            print("next_node is None") 

        current.next_node = prev # current = 1, current.next_node = None -- 1, 2

        if current.next_node != None:
            print(f"current.next_node is: {current.next_node.get_value()}")
        else:
            print("current.next_node is None")

        prev = current # was None, now = 1 -- 2, 3

        if prev != None:
            print(f"prev is: {prev.get_value()}")
        else:
            print("prev is None")

        current = next_node # 2 -- 3, None

        if current != None:
            print(f"current is: {current.get_value()}")
        else:
            print("current is None")

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




