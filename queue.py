# import linked list
from linked import LinkedList


class Queue:
    # construct queue
    def __init__(self, m):
        self.llist = LinkedList(m)
        self.nodes = 0

    # add node to back of queue
    def enqueue(self, node):
        self.llist.add_tail(node)
        self.nodes = self.llist.length()

    # remove node from front of queue and return the value
    def dequeue(self):
        node = self.llist.delete_head()
        self.nodes = self.llist.length()
        return node

    # return true if queue is full
    def isFull(self):
        self.llist.full()

    # return true if queue is empty
    def isEmpty(self):
        self.llist.empty()

    # delete entire queue
    def clear(self):
        self.llist = None

    # look at front of queue without deleting
    def poll(self):
        return self.llist.head

    # print entire queue
    def output(self):
        curr = self.llist.tail
        while curr is not None:
            print(curr.data)
            curr = curr.prev
        return


