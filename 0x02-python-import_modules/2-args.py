#!/usr/bin/python3
# print its arguments

if __name__ == "__main__":
    """Print the addition of all arguments"""
    import sys

    if len(sys.argv) == 1:
        print("0 arguments")
    elif len(sys.argv) == 2:
        print("1 argument\n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(sys.argv[i], i))
