class StackParenthesesChecker:
    def isBalanced(self, stack):
        #initialize counters
        lcounter = 0
        rcounter = 0
        #initialize current node
        curr = stack.llist.head
        #loop until current is None
        while curr is not None:
            #check if curr is '(' or ')'
            if curr.data == '(':
                lcounter += 1
            elif curr.data == ')':
                rcounter += 1
            #add to counter if yes
            curr = curr.prev
        #if both counters are equal but not 0, return true
        if rcounter == lcounter and lcounter != 0 and rcounter != 0:
            return True
        else:
            return False
            
        
