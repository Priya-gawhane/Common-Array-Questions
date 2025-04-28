def merge_arrays(arr1, arr2):
    arr3 = arr1 + arr2
    arr3.sort()
    return arr3

arr1 = [1, 3, 5, 9]
arr2 = [2, 1, 6, 8]
arr3 = merge_arrays(arr1, arr2)

for value in arr3:
    print(value, end=" ")
