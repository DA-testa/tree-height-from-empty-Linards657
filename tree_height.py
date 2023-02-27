# python3

import sys
import threading
import re
import numpy as np


def iteration(i, parents, root):
    global newMax
    backlog = np.where(parents == root)[0]
    i = i + 1
    for x, value in enumerate(backlog):
        iteration(i, parents, backlog[x])
    if i > newMax:
        newMax = i
    else:
        return


def compute_height(n, parents):
    # Write this function
    max_height = 0
    root = np.where(parents == -1)[0]
    iteration(max_height, parents, root)
    # Your code here
    return newMax


def main():
    # implement input form keyboard and from files
    global newMax
    newMax = 0
    text = input()
    if "I" in text[:1]:
        count = input()
        array = np.asarray(list(map(int, input().split())))
        print(compute_height(count, array))
    else:
        text = input()
        if not re.search("^a", text):
            f = open("./test/" + text, "r")
            count = f.readline()
            array = np.asarray(list(map(int, f.readline().split())))
            f.close()
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
