def find_smallest_int(arr):
    # Code here
    smallest = arr[0]

    for i in range(1,len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
    return smallest

