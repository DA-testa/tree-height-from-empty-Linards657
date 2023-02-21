# python3

import sys
import threading
import numpy as np
import re


def compute_height(n, parents):
    # Write this function
    check = True
    backlog = []
    iterator = 0
    max_height = 0
    lastRemembered = 0
    for i in range(parents.size):
        if -1 == parents[i]:
            root = i;
    while check:
        backlogbool = list(map(lambda x: x == root, parents))
        for x in range(len(backlogbool)):
            if backlogbool[x]:
                backlog.append(x)
        root = backlog.pop()
        iterator = iterator +1
        if max_height < iterator:
            max_height = iterator
        if not backlog:
            check = False
        if len(backlog) > lastRemembered:
            lastRemembered = len(backlog)
            savedIterator = iterator
        if lastRemembered > len(backlog):
            lastRemembered = len(backlog)
            iterator = savedIterator
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    if "I" in text[:1]:
        count = input()
        array = np.asarray(list(map(int, (input().split()))))
        print(compute_height(count, array))
    else:
        if not re.search("^a", text):
            f = open(".\\" + text, "r")
            count = f.readline()
            array = np.asarray(list(map(int, (f.readline.split()))))
            print(compute_height(count, array))

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
