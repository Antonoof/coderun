import sys

def main():
    a, b = map(int, input().split())
    r1 = 0
    r2 = a * b

    if a > b:
        b, a = a, b

    while a != 0 and b != 0:
        b = b % a
        b, a = a, b

    r1 = a + b
    r2 //= r1
    print(r1, r2)

if __name__ == '__main__':
    main()
