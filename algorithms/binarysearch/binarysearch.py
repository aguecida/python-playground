from random import randint

def binary_search(range_min, range_max):
    '''
    Performs a binary search to find a randomly selected number between a range of two integers.

    Args:
        range_min: The lowest possible value of the randomly selected integer.
        range_max: The highest possible value of the randomly selected integer.

    Returns:
        guess: The correct guess.
        tries: The number of tries it took to find the number.
    '''
    random_num = randint(range_min, range_max)
    tries = 0
    prev_guess = None

    while True:
        guess = int((range_min + range_max) / 2)
        tries += 1

        # Make sure we don't get stuck in a loop since guess operation is always rounded down
        if guess == prev_guess:
            guess += 1

        if guess > random_num:
            range_max = guess
        elif guess < random_num:
            range_min = guess
        else:
            break

        prev_guess = guess

    return guess, tries

if __name__ == '__main__':
    try:
        range_min = int(input('Enter min range: '))
        range_max = int(input('Enter max range: '))
    except:
        print('Received bad input, exiting...')
        quit()

    correct_guess, num_tries = binary_search(range_min, range_max)

    if num_tries == 1:
        print(f'Found number {correct_guess} in {num_tries} try!')
    else:
        print(f'Found number {correct_guess} in {num_tries} tries!')
