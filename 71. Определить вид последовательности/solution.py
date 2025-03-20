import sys

def main():
    x = int(input())
    arr = []

    while x != -2000000000:
        arr.append(x)
        x = int(input())

    sort_arr = sorted(arr)
    asc = desc = 1

    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            asc = 0
            break

    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            desc = 0
            break

    if len(set(arr)) == 1:
        print('CONSTANT')
    elif asc:
        print('ASCENDING')
    elif desc:
        print('DESCENDING')
    elif sort_arr == arr:
        print('WEAKLY ASCENDING')
    elif sort_arr[::-1] == arr:
        print('WEAKLY DESCENDING')
    else:
        print('RANDOM')

if __name__ == '__main__':
    main()
