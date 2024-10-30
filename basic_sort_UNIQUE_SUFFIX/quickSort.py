def sectionING(arr, low, high):
    """
    Partitions the array `arr` for the quicksort algorithm.
    
    :param arr: List of elements to be sorted.
    :param low: Starting index of the segment to partition.
    :param high: Ending index of the segment to partition.
    :returns: The partition index `i + 1` after positioning elements less than the pivot to the left
              and those greater than the pivot to the right.
    
    **Algorithm**:
    - Selects the last element in the segment as the pivot.
    - Moves all elements smaller than the pivot to the left of the pivot's final position.
    - Returns the final index of the pivot.
    """
    
    pivot = arr[high]  # Pivot element
    
    i = low - 1  # Pointer for the smaller element index
    
    # Traverse elements in the current range
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swapING(arr, i, j)  # Swap if element is smaller than the pivot
    
    # Move the pivot to its correct position
    swapING(arr, i + 1, high)
    return i + 1


def swapING(arr, i, j):
    """
    Swaps two elements in the array.
    
    :param arr: List of elements.
    :param i: First index for the swap.
    :param j: Second index for the swap.
    """
    arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr, low, high):
    """
    Sorts the array `arr` using the quicksort algorithm.
    
    :param arr: List of elements to be sorted.
    :param low: Starting index of the segment to sort.
    :param high: Ending index of the segment to sort.
    
    **Algorithm**:
    - If the segment contains more than one element, partition the array.
    - Recursively apply quicksort to the left and right subarrays of the pivot.
    """
    if low < high:
        si = sectionING(arr, low, high)  # Partitioning index
        
        # Recursively sort elements before and after partition
        quickSort(arr, low, si - 1)
        quickSort(arr, si + 1, high)
