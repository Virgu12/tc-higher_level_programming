#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numsm = 0
    for nmr in range(1, len(sys.argv)):
        numsm += int(sys.argv[nmr]) 
    print(numsm)
