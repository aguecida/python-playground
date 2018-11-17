inputs = { '1': ' ',  '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' ' }

players = { '1': '', '2': '' }


def player_pick_symbol():
    symbol = ''

    while symbol == '':
        symbol = input('Player 1 select your symbol (x/o): ')

        if symbol == 'x':
            players['1'] = 'x'
            players['2'] = 'o'
        elif symbol == 'o':
            players['1'] = 'o'
            players['2'] = 'x'
        else:
            print('You entered an invalid symbol! Please select "x" or "o"')
            symbol = ''

    print(f'Player 1 is {players["1"]}')
    print(f'Player 2 is {players["2"]}')
        

def print_board_configuration():
    print('     |     |     ')
    print('  7  |  8  |  9  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  4  |  5  |  6  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  1  |  2  |  3  ')
    print('     |     |     ')

def print_board(inputs):
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(inputs['7'], inputs['8'], inputs['9']))
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(inputs['4'], inputs['5'], inputs['6']))
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(inputs['1'], inputs['2'], inputs['3']))
    print('     |     |     ')

player_pick_symbol()
#print_board_configuration()
#print_board(inputs)

