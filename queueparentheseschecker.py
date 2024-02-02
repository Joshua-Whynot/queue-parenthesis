class QueueParenthesesChecker:
    def isBalanced(self, q1, q2):
        # initialize rcounter and lcounter
        rcounter = 0
        lcounter = 0
        # loop through for how many nodes exist in q1
        for i in range(q1.nodes):
            # remove all but one node from q1
            for i in range(q1.nodes - 1):
                q2.enqueue(q1.dequeue())
                i += 1
            # remove last value in q1
            temp = q1.dequeue().data
            # check if temp has either '(' or ')'
            if temp == "(":
                lcounter += 1
            elif temp == ")":
                rcounter += 1
            # if it has either, add one to the counter
            # set q1 back to the remainder of q2
            x = q1
            q1 = q2
            q2 = x
        # check if rcounter and lcounte are equal but not equal to 0
        if rcounter == lcounter and lcounter != 0 and rcounter != 0:
            return True
        else:
            return False

