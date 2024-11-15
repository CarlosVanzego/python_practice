def in_order(arr):
    # Outer loop: iterates over each element of the array  
    for i in range(len(arr)):
        # Assumes the current element is the smallest (minVal is the index of the smallest element found)    
        min_val = i
        # Inner loop: iterates through the unsorted portion of the array to find the smallest element    
        for s in range(i + 1, len(arr)):
            # if the smaller element is found, updates min_val to that element's index      
            if arr[s] < arr[min_val]:
                min_val = s
        
        # Swap elements
        temp = arr[i]  # Temporarily stores the current element
        arr[i] = arr[min_val]  # Replace the current element with the smallest found
        arr[min_val] = temp  # Place the current element where the smallest was
    
    return arr

arr = [100, 7, 2, 13, 17, 6, 5, 4]
print(in_order(arr))  # [2, 4, 5, 6, 7, 11, 12, 13]

