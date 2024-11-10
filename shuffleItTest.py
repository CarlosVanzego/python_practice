def shuffle_it(arr, *c):
    # Iterate over each pair of indices in c
    for pair in c:
        # Get the first index of the current pair
        a = pair[0]
        # Get the second index of the current pair
        b = pair[1]
        # Swap the elements at indices a and b in the array     
        arr[a], arr[b] = arr[b], arr[a]
    return arr

print(shuffle_it([1, 2, 3, 4, 5], [1, 2]))
print(shuffle_it([1, 2, 3, 4, 5], [1, 2], [3, 4]))
print(shuffle_it([1, 2, 3, 4, 5], [1, 2], [3, 4], [2, 3]))

