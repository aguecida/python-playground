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

inputs = { '1': ' ',  '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' ' }

print_board_configuration()
print_board(inputs)

