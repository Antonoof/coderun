import sys


def main():
    n = int(input())
    res = []

    for x in range(n):
        res.append(input().split())

    find_word = input()

    for w1, w2 in res:
        if w1 == find_word:
            print(w2)
            break
        if w2 == find_word:
            print(w1)
            break

if __name__ == '__main__':
    main()
