#Two Sum – Pair with given Sum
#Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target. This problem is a variation of 2Sum problem.

def twoSum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == target:
                return True
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, -4]
    target = 2

    if twoSum(arr, target):
        print("true")
    else:
        print("false")
