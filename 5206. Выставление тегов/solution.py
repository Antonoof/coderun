import sys

def main():
    inp = int(input())
    res = 0
    m1 = 0
    m2 = 1

    for _ in range(inp):
        res += m1 + m2
        m2, m1 = m1, m1 + m2

    print(res)

if __name__ == '__main__':
    main()
