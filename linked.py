class LinkedList:
    # construct linked list with max nodes based on string length passed into main
    def __init__(self, m):
        self.head = None
        self.tail = None
        self.maxNodes = m
        self.nodes = 0

    # add a head to the linked list
    def add_head(self, node):
        # if the list is full tell user
        if self.full() != True:
            if self.nodes == 0:
                # if list has no nodes set tail and head to new node
                self.head = node
                self.tail = node
            else:
                # if list is populated set prev to old head and new head to new node
                node.prev = self.head
                self.head.next = node
                self.head = node
            # increment node amount
            self.nodes += 1
        else:
            print("Linked List is Full")

    # add a tail to the linked list
    def add_tail(self, node):
        # check if list is full, if it is tell user
        if self.full() != True:
            if self.nodes == 0:
                # if list has no nodes set tail and head to new node
                self.head = node
                self.tail = node
            else:
                # if list is populated set prev to old tail and new tail to new node
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            # increment node amount
            self.nodes += 1
        else:
            print("Linked List is Full")

    # code to delete head
    def delete_head(self):
        # check if list is empty
        if self.empty() != True:
            # if amount of nodes is 1, delete head and tail
            if self.nodes == 1:
                temp = self.head
                self.head = None
                self.tail = None
            else:
                # delete head while setting node that head points to as new head
                temp = self.head
                self.head = self.head.next
                self.head.prev.next = None
                self.head.prev = None
            # decrement node counter
            self.nodes -= 1
            return temp
        else:
            # tell user if list is empty
            print("Linked List is Empty")

    def delete_tail(self):
        # check if list is empty
        if self.empty() != True:
            # if amount of nodes is 1, delete head and tail
            if self.nodes == 1:
                temp = self.tail
                self.head = None
                self.tail = None
            else:
                # delete tail while setting node that tail points to as new tail
                temp = self.tail
                self.tail = self.tail.prev
                self.tail.next.prev = None
                self.tail.next = None
            # decrement node counter
            self.nodes -= 1
            return temp
        else:
            # tell user if list is empty
            print("Linked list is Empty")

    def full(self):
        # return true if nodes = maxNodes
        if self.nodes == self.maxNodes:
            return True
        else:
            return False

    def empty(self):
        # return true if nodes = 0
        if self.nodes == 0:
            return True
        else:
            return False

    def length(self):
        # return node amount
        return self.nodes

