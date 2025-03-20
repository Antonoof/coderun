import sys

def main():
    xyz = set(input().split())
    line = set(input())

    line -= xyz

    print(len(line))

if __name__ == '__main__':
    main()
