def findDuplicates(arr):
    freqMap = {}
    result = []

    for num in arr:
        freqMap[num] = freqMap.get(num, 0) + 1

    for key, value in freqMap.items():
        if value > 1:
            result.append(key)

    if not result:
        result.append(-1)
    return result

if __name__ == "__main__":
   arr = [1, 5, 6, 9, 5, 1, 2, 5]
   duplicates = findDuplicates(arr)

   for element in duplicates:
       print(element, end=" ")
