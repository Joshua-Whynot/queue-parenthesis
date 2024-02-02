class Node:
    
    #construct node, data is passed in from main
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.id = None

    def get_data(self):
        #return data
        return self.data