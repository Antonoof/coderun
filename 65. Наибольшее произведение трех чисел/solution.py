import sys

def main():
    arr = list(map(int, input().split()))

    arr.sort()
    
    if (arr[0] * arr[1] * arr[-1]) > (arr[-1] * arr[-2] * arr[-3]):
        print(arr[0], arr[1], arr[-1])
    else:
        print(arr[-3], arr[-2], arr[-1])

if __name__ == '__main__':
    main()
