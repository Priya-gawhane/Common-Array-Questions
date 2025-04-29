def leftRotation(a, d):
    n = len(a)
    d = d % n
    rotated_array = a[d:] + a[:d]
    return rotated_array

if __name__ == "__main__":
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    result = leftRotation(a, d)
    print(' '.join(map(str, result)))
