def largestNumber(arr):
   
    for i in range(1, len(arr)):
        if arr[0] < arr[i]:
            arr[0] = arr[i]

    return arr[0]

if '__name__' == '__main__':

    array = [1, 512, 52, 151761421, 516, 515, 152, 6327, 517,25255]
    print(largestNumber(array))
   