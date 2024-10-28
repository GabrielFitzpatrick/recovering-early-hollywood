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
    qsort docstring
    """
    print("quick sort")


def insertion(int_list):
    """
    insertion docstring
    """
    print("insertion sort")
