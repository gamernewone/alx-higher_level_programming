#!/usr/bin/python3
# print all names defined by hidden_3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
