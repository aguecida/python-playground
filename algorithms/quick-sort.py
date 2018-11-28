def quick_sort(lst, low = None, high = None):
    '''
    Sorts a list of integers using the Quick Sort algorithm.
    This implementation uses the last element in the list as the pivot.

    Args:
        lst: A list of integers to sort.
        low: The lower bound of the current partition.
        high: The high bound of the current partition.

    Returns:
        The sorted list of integers.
    '''
    # For first iteration, set limits as the bounds of the entire list
    if low is None and high is None:
        low = 0
        high = len(lst) - 1

    # Only sort if there is more than 1 element in the current partition
    if low < high:
        # Pick pivot element and initialize pivot insertion index
        pivot = lst[high]
        index = low - 1

        # Sort elements around partition element and position pivot index
        for i in range(low, high):
            if lst[i] <= pivot:
                index += 1 
                lst[i], lst[index] = lst[index], lst[i]

        # Put the pivot element in it's final position
        lst[index + 1], lst[high] = lst[high], lst[index + 1]

        # Run quick sort recursively on sublists on each side of the pivot element
        quick_sort(lst, low, index - 1)
        quick_sort(lst, index + 1, high)

    return lst

if __name__ == '__main__':
    user_input = input('Enter comma separated list of integers to sort: ')

    try:
        user_input = user_input.split(',')
        user_input = [ int(num) for num in user_input ]
    except:
        print('\nReceived bad input, exiting...')
        quit()
    
    print(f'\nApplying quick sort to list: {user_input}')

    sorted_list = quick_sort(user_input)

    print(f'\nSorted list: {sorted_list}')
