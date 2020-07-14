<<<<<<< Updated upstream
=======
# from stack import LinkedList
# from linked_list import LinkedList

# import sys
# sys.path.append("/Users/scott/dev/lambda/CS/Data-Structures/singly_linked_list")
# from singly_linked_list import LinkedList

import os
import sys
sys.path.append(f'{os.getcwd()}/singly_linked_list')
from singly_linked_list import LinkedList, Node

>>>>>>> Stashed changes
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?

    def __len__(self):
        return self.size
        # current = self.storage.head
        # count = 0
        # while current:
        #     current = current.get_next()
        #     count += 1
        # return count

    def push(self, value):
        self.size += 1
        return self.storage.prepend(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_head()
