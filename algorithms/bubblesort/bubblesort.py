def bubble_sort(lst):
    '''
    Sorts a list of integers using the bubble sort algorithm.
    Note: The list is sorted in place.

    Args:
        lst: A list of integers to sort.

    Returns:
        iterations: The number of iterations it took to sort the list.
    '''
    iterations = 0
    
    while True:
        swapped = False
        iterations += 1

        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
                swapped = True

        if not swapped:
            break

    return iterations

if __name__ == '__main__':
    user_input = input('Enter comma separated list of integers to sort: ')

    try:
        user_input = user_input.split(',')
        user_input = [ int(num) for num in user_input ]
    except:
        print('Received bad input, exiting...')
        quit()
    
    print(f'\nApplying bubble sort to list: {user_input}')

    iterations = bubble_sort(user_input)

    if iterations == 1:
        print(f'\nSorted list = {user_input} in {iterations} iteration')
    else:
        print(f'\nSorted list = {user_input} in {iterations} iterations')
