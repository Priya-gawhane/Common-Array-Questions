#using sum of n terms formula

def missingNum(arr):
    n = len(arr) + 1
    totalsum = sum(arr)
    expsum = n * (n + 1) // 2
    return expsum - totalsum

if __name__ == "__main__":
    arr = [8, 6, 5, 4, 1, 3, 7]
    print(missingNum(arr))
