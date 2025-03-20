import sys
from collections import defaultdict

def main():
    lines = sys.stdin.readlines()
    d = defaultdict(int)

    for line in lines:
        for word in line.split():
            print(d[word], end=' ')

            d[word] += 1

if __name__ == '__main__':
    main()
