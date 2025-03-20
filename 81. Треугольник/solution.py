import sys

def main():
    t1, t2, t3 = (int(input()) for _ in range(3))

    if t1 + t2 > t3 and t2 + t3 > t1 and t1 + t3 > t2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
