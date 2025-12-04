#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        arg = sys.argv[1]
        print("1 argument:")
        print(f"1: {arg}")
    else:
        print(f"{num_args} arguments:")
        for argmts in range(1, len(sys.argv)):
            print(f"{argmts}: {sys.argv[argmts]}")
