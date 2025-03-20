import sys

def main():
    n = int(input())
    arr = input().split()
    idx = 0

    for i in range(n):
        if arr[i:] == arr[i:][::-1]:
            break

        idx += 1

    print(idx)
    print(" ".join(arr[:idx][::-1]))

if __name__ == '__main__':
    main()
