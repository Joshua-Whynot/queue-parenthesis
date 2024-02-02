# CS3310 Spring Assignment 1 Western Michigan University
# Author: Joshua Whynot
# Date: 2/2/2024
# imports
from node import Node
from queue import Queue
from stack import Stack
from stackparentheseschecker import StackParenthesesChecker
from queueparentheseschecker import QueueParenthesesChecker

# main function
def main():
    # init run flag
    run = True
    # loop to continually run program until user wants to exit
    while run == True:
        # take input
        userString = input("Enter string: ")
        # initialize queues and stacks with max length based on length of input string
        queue1 = Queue(range(len(userString)))
        queue2 = Queue(range(len(userString)))
        stack = Stack(range(len(userString)))
        # initialize stack and queue checkers
        stackChecker = StackParenthesesChecker()
        queueChecker = QueueParenthesesChecker()

        # initialize i
        i = 0
        # for loop to populate stack
        for i in range(len(userString)):
            index = i
            node = Node(userString[i])
            stack.push(node)

        # for loop to populate queue1
        for i in range(len(userString)):
            index = i
            node = Node(userString[i])
            queue1.enqueue(node)
        # check if string is balanced using stack checker and queue checker (pass only if both are true)
        if (
            stackChecker.isBalanced(stack) == True
            and queueChecker.isBalanced(queue1, queue2) == True
        ):
            # output to user
            print("The input string {} has balanced parentheses.".format(userString))
        else:
            # output to user
            print(
                "The input string {} does not have balanced parentheses.".format(
                    userString
                )
            )

        # ask if user would like to enter a new string
        res = input("Would you like to enter another string? (Y/N): ")
        # if user replied anything but 'y' or 'Y' the program will close
        if res.upper() != "Y":
            print("program exiting")
            run = False


if __name__ == "__main__":
    main()

