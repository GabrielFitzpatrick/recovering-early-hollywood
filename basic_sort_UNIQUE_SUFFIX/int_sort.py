# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers...
"""


def bubble(int_list):
    print("bubble sort")
    """
    Bubble sort works by repeatedly stepping through the list, comparing each pair of
    adjacent elements and swapping them if they are in the wrong order. The pass through
    the list is repeated until the list is sorted.

    Parameters:
        int_list (list): A list of comparable elements to be sorted
    
    Returns:
        list: The sorted list in ascending order
    
    Example:
        >>> bubble([5, 3, 8, 4, 2])
        [2, 3, 4, 5, 8]

    Time Complexity:
        Best case: O(n) when list is already sorted
        Worst and Average Case: O(n^2) due to nested loops

    Space Complexity:
        O(1), since it is an in-place sorting algorithm
    """
    n = len(int_list)
    for i in range(n):
        # Track if any swaps made in this iteration
        swapped = False
        # Bubble up process
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
                swapped = True # Swap if in wrong order
        # If no swaps, array is already sorted
        if not swapped:
            break
    return int_list


def quick(int_list):
    """
    Sorts an array of elements in ascending order using the quick sort algorithm.

    Quick sort is a divide-and-conquer algorithm that selects a pivot element and partitions
    the array into two halves, one with elements less than the pivot and one with elements 
    greater than the pivot. It then recursively sorts the partitions.

    Parameters:
        int_list (list): A list of comparable elements to be sorted.
    
    Returns:
        list: The sorted list in ascending order.

    Example:
        >>> quick([5, 3, 8, 4, 2])
        [2, 3, 4, 5, 8]

    Time Complexity:
        Best and Average Case: O(n log(n))
        Worst Case: O(n^2) when the array is already sorted in order or reverse order

    Space Complexity:
        O(log(n)) due to recursive function calls for partitioning
    """
    print("quick sort")
    
    def _quick_sort_recursive(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high) # Partition array and get pivot index
            # Recursively sort elements before and after partition
            _quick_sort_recursive(arr, low, pivot_index - 1)
            _quick_sort_recursive(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        """
        This function takes the last element as a pivot, places the pivot
        element at its correct position in the sorted array, and places all
        elements smaller than the pivot to the left and all greater elements
        to the right

        Parameters:
            arr (list): The list to partition
            low (int): The starting index of the partition
            high (int): The ending index of the partition

        Returns:
            int: The index of the pivot element after partitioning
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Initial call to _quick_sort_recursive
    _quick_sort_recursive(int_list, 0, len(int_list) - 1)
    return int_list


def insertion(int_list):
    """
    Sorts an array of elements in ascending order using the insertion sort algorithm.

    Insertion sort is a simple, stable sorting algorithm that builds the sorted list one
    element at a time by comparing and inserting each element in its correct position.

    Parameters:
        int_list (list): A list of comparable elements to be sorted

    Returns:
        list: The sorted list in ascending order
    
    Example:
        >>> insertion_sort([5, 3, 8, 4, 2])
        [2, 3, 4, 5, 8]

    Time Complexity:
        Best Case: O(n) when the list is already sorted
        Worst and Average Case: O(n^2) due to nested loops

    Space Complexity:
        O(1), since it is an in-place sorting algorithm
    """
    print("insertion sort")

    for i in range(1, len(int_list)):
        key = int_list[i] # The current element to be inserted in the sorted part
        # Shift elements of int_list[0...i-1] that are > key to one position ahead
        j = i - 1
        while j >= 0 and int_list[j] > key:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = key # Insert key element at correct position
    return int_list
