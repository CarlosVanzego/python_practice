def in_order_faster(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the midpoint and split the array into left and right halves
    mid = len(arr) // 2
    left = in_order_faster(arr[:mid])
    right = in_order_faster(arr[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # Compare elements from left and right arrays and add the smallest one to the sorted_array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # Append any remaining elements from both halves
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

arr = [9, 3, 12, 1, 6, 4, 3, 2]
print(in_order_faster(arr))  



