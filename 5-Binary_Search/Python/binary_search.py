def binarySearch(arr, key):
    key = int(key)
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = int((low + high) / 2 )
        if key == arr[mid]:
            return mid
        elif key > arr[mid] :
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    array = [1, 2, 3, 4, 62, 5, 81]

    sorted(array)

    key = input("Enter search key: ")

    res = binarySearch(array, key)
    if res > -1 :
        print('Number', key, 'is FOUND at index: ', res)
    else:
        print('Number', key, 'is NOT FOUND')

