def bubble_sort(lst):
    '''
    Sorts a list of integers using the bubble sort algorithm.

    Args:
        lst: A list of integers.

    Returns:
        The sorted list.
    '''
    list_length = len(lst)
    pass_num = 0

    while True:
        swapped = False
        pass_num += 1

        for i in range(list_length):
            if i != list_length - 1 and lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
                swapped = True

        print(f'\nList after pass #{pass_num}: {lst}')

        if not swapped:
            break

    return lst

if __name__ == '__main__':
    user_input = input('Enter comma separated list of integers to sort: ')

    try:
        user_input = user_input.split(',')
        user_input = [ int(num) for num in user_input ]
    except:
        print('Received bad input, exiting...')
        quit()
    
    print(f'\nApplying bubble sort to list: {user_input}')

    bubble_sort(user_input)
