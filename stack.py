#import linked list
from linked import LinkedList

class Stack:
    # construct stack based on linked list
    def __init__(self, m):
        self.llist = LinkedList(m)
        self.nodes = 0

    # push element to top of stack
    def push(self, node):
        self.llist.add_head(node)
        self.nodes = self.llist.length()

    # pop element from top of stack and return it
    def pop(self):
        node = self.llist.delete_head()
        self.nodes = self.llist.length()
        return node

    # check if stack is full
    def isFull(self):
        self.llist.full()

    # check if stack is empty
    def isEmpty(self):
        self.llist.empty()

    # clear stack
    def clear(self):
        self.llist = None

    # check top element without deleting
    def peek(self):
        return self.llist.head

    # print entire stack
    def output(self):
        curr = self.llist.head
        while curr is not None:
            print(curr.data)
            curr = curr.prev
        return

