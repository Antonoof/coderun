import sys

def main():
    lines = sys.stdin.readlines()
    s = set()

    for line in lines:
        s |= set(line.split())

    print(len(s))

if __name__ == '__main__':
    main()
