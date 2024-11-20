def in_order_faster(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr  # Return the array as is since it doesn't need sorting
    
    # Find the midpoint of the array to divide it into two halves
    mid = len(arr) // 2  # Integer division to find the middle index
    
    # Recursively sort the left half of the array
    left = in_order_faster(arr[:mid])  # Slice the array from the start to the midpoint
    
    # Recursively sort the right half of the array
    right = in_order_faster(arr[mid:])  # Slice the array from the midpoint to the end
    
    # Merge the two sorted halves and return the result
    return merge(left, right)  # Call the merge function to combine sorted halves

def merge(left, right):
    # Initialize an empty list to store the sorted elements
    sorted_array = []
    
    # Initialize pointers for the left and right arrays
    i = j = 0  # i tracks the index for the left array, j for the right array
    
    # Compare elements from both arrays and append the smallest to sorted_array
    while i < len(left) and j < len(right):  # Continue until one of the arrays is exhausted
        if left[i] < right[j]:  # Compare current elements in left and right arrays
            sorted_array.append(left[i])  # Add the smaller element to the sorted list
            i += 1  # Move the pointer for the left array forward
        else:
            sorted_array.append(right[j])  # Add the smaller element to the sorted list
            j += 1  # Move the pointer for the right array forward
    
    # Add any remaining elements from the left array to the sorted list
    sorted_array.extend(left[i:])  # This happens if the left array has elements left
    
    # Add any remaining elements from the right array to the sorted list
    sorted_array.extend(right[j:])  # This happens if the right array has elements left
    
    return sorted_array  # Return the merged and sorted array

# Example array to be sorted
arr = [9, 3, 12, 1, 6, 4, 3, 2]  # Unsorted input array

# Print the sorted result of the array using in_order_faster
print(in_order_faster(arr))  # Expected output: [1, 2, 3, 3, 4, 6, 9, 12]



