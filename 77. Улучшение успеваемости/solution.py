import sys
from math import ceil

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    total_score = 2 * a + 3 * b + 4 * c
    total_count = a + b + c
    # если вы пытались поделить на 1.5 то ошибка будет float
    result = (7 * total_count - 2 * total_score) / 3

    if result > 0:
        print(ceil(result))
    else:
        print(0)

if __name__ == '__main__':
    main()
