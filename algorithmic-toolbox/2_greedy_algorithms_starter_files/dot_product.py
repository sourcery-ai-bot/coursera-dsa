# Uses python3
import sys


def min_dot_product(a, b):
    a.sort()
    b.sort(reverse=True)
    return sum(a[i] * b[i] for i in range(len(a)))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
