#!/usr/bin/python3
import hidden_4


def finders():
    dirname = dir(hidden_4)
    for i in dirname:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    finders()
