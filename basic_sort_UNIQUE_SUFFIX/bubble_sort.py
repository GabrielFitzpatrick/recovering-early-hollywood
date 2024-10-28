def bubble_sort(arr):
    """
    Sorts an array of elements in ascending order using the bubble sort algorithm

    Parameters:
        arr (list): A list of comparable elements to be sorted

    Returns:
        list: The sorted list in ascending order
    
    Time complexity:
        Best case: O(n) when the list is already sorted
        Worst and average case: O(n^2) due to nested loops
    
    Space complexity:
        O(1), since it is an in-place sorting algorithm
    """

    n = len(arr)
    for i in range(n):
        # Track any swaps made in this iteration
        swapped = False
        # Perform bubble up process
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap if in wrong order
                swapped = True
        # If no swaps made, array is already sorted
        if not swapped:
            break
    return arr