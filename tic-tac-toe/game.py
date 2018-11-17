inputs = { '1': ' ',  '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' ' }
players = { '1': '', '2': '' }
players_turn = 1


def game():
    '''
    The main game entry point
    '''
    print('Welcome to the game of Tic-Tac-Toe!\n')

    # Setup game
    print_board_configuration()
    player_pick_symbol()

    # Main game loop
    while True:
        player_move()
        print_board()
        status = get_game_status()

        if status['gameover']:
            if status['winner'] in [1,2]:
                print(f"\nGAME OVER! Player {status['winner']} wins!")
            else:
                print("\nGAME OVER! It's a tie!")
            break

        end_players_turn()


def get_game_status():
    '''
    Checks if the game is over and if there is a winner.

    Returns:
        gameover: A boolean specifying whether or not the game is over.
        winner: The number of the winning player, or "None" if the game is a tie.
    '''
    if check_horizontal() or check_vertical() or check_diagonal():
        return { 'gameover': True, 'winner': players_turn }

    # Check for full board
    for value in inputs.values():
        if value != 'x' and value != 'o':
            return { 'gameover': False, 'winner': None }
    
    return { 'gameover': True, 'winner': None }


def check_horizontal():
    return (inputs['1'] == inputs['2'] == inputs['3'] != ' ') or (inputs['4'] == inputs['5'] == inputs['6'] != ' ') or (inputs['7'] == inputs['8'] == inputs['9'] != ' ')


def check_vertical():
    return (inputs['1'] == inputs['4'] == inputs['7'] != ' ') or (inputs['2'] == inputs['5'] == inputs['8'] != ' ') or (inputs['3'] == inputs['6'] == inputs['9'] != ' ')


def check_diagonal():
    return (inputs['1'] == inputs['5'] == inputs['9'] != ' ') or (inputs['3'] == inputs['5'] == inputs['7'] != ' ')


def end_players_turn():
    '''
    Changes the players turn.
    '''
    global players_turn

    if players_turn == 1:
        players_turn = 2
    else:
        players_turn = 1


def player_move():
    '''
    Takes the players move as an input and updates the board accordingly
    '''
    move = None
    symbol = players[str(players_turn)]

    while move == None:
        move = input(f'Player {players_turn}, enter your move (1-9): ')
        if int(move) >= 1 and int(move) <= 9:
            inputs[move] = symbol
        else:
            print('You entered an invalid move! Please select a number between 1 and 9.')
            move = None


def player_pick_symbol():
    '''
    Takes a player's input to determine which players will use which symbols.
    '''
    symbol = None

    while symbol == None:
        symbol = input('Player 1 select your symbol (x/o): ')

        if symbol == 'x':
            players['1'] = 'x'
            players['2'] = 'o'
        elif symbol == 'o':
            players['1'] = 'o'
            players['2'] = 'x'
        else:
            print('You entered an invalid symbol! Please select "x" or "o".')
            symbol = None

    print('\n')
    print(f'Player 1 is {players["1"]}')
    print(f'Player 2 is {players["2"]}')
    print('\n')
        

def print_board_configuration():
    '''
    Draws the game board configuration.
    '''
    print('BOARD CONFIGURATION:\n')
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
    print('\n')


def print_board():
    '''
    Draws the current state of the board given player inputs.
    '''
    global inputs

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


game()
