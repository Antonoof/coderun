import sys

def main():
    A, B, C, D, E = (int(input()) for _ in range(5))

    if (A <= D and B <= E) or (A <= E and B <= D) or \
       (B <= D and C <= E) or (B <= E and C <= D) or \
       (A <= D and C <= E) or (A <= E and C <= D):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
