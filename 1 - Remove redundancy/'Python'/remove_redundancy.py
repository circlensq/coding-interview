def removeRedundancy(arr):
    j = 0
    
    for i in range(0, len(arr)):
       
        if i == len(arr)-1 and arr[i] != arr[i-1]:
            arr[j] = arr[i]
            
        elif arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1
        
    return arr, j 

if '__name__' == '__main__':
    array = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8 ]
    # ! Still Error, need to be improved when array
    # ! array [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8]

    new_arr, length = removeRedundancy(array)
    for i in range(length+1):
        print(new_arr[i])