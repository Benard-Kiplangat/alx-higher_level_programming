#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argc = len(sys.argv)
    for i in range(argc):
        if i == 0:
            continue
        sum = sum + int(sys.argv[i])
    print(f"{sum}")
