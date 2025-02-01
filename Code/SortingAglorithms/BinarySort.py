def binarySort(array, key, offset=0):
    if not array:
        return -1 # If key not found, return -1
    
    # If slice has one element, check it directly.
    if len(array) == 1:
        return offset if array[0] == key else -1
    
    midIndex = len(array) // 2
    middleValue = array[midIndex]
    
    # Check if we've found the key.
    if middleValue == key:
        return offset + midIndex
    elif middleValue < key:
        # Search the right half, update the offset.
        return binarySort(array[midIndex + 1:], key, offset + midIndex + 1)
    else:
        # Search the left half.
        return binarySort(array[:midIndex], key, offset)

# Example usage:
print(binarySort([], 2))
