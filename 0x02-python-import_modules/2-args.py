#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    elif argc > 2:
        print(f"{argc - 1} arguments:")
        for i in range(argc):
            if i == 0:
                continue
            print(f"{i}: {sys.argv[i]}")
    else:
        print("0 arguments.")
