###################################

row = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# row = ['1','2','3','4','5','6','7','8','9']

srow1 = ['1','2','3']
srow2 = ['4','5','6']
srow3 = ['7','8','9']

players = {'player1':'', 'player2':''}
players_list = ['player1', 'player2']

locations = ['1','2','3','4','5','6','7','8','9']

start = ''
play = True
playing = 0

####################################

def intro():
    print('Hello, welcome!!')
    print('This is a two player game of TicTacToe\n')
    global start 
    start = input('Enter "Y" to Start or any key to quit: ')
    print('You can also quit the game at any time by clicking "Q"')

def decide_start():
    if start == 'y' or start == 'Y':
        start_game()
    else:
        print('\n Goodbye :( \n')

def start_game():
    refresh()
    allocate_player()
    print_board(row,srow1,srow2,srow3)
    game_play()

def refresh():
    global row
    global players
    global locations
    global start
    global play
    global playing

    row = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    players = {'player1':'', 'player2':''}

    locations = ['1','2','3','4','5','6','7','8','9']

    start = ''
    play = True
    playing = 0

def allocate_player():
    global players
    select = '1'
    temp = ['X','x','O','o']
    while select not in temp:
        print()
        select = input('Player1 select X or O: ')
        if select not in temp:
            print('Invalid selection try again')
    
    if select == 'X' or select == 'x':
        players['player1'] = 'X'
        players['player2'] = 'O'
    else:
        players['player1'] = 'O'
        players['player2'] = 'X'
    
    print()
    print('Player1 = {}'.format(players['player1']))
    print('Player2 = {}'.format(players['player2']))
    print()

def print_board(row1,srow1,srow2,srow3):
    print('\n                 Game Board                \n')
    temp = '                       '
    print(' | '.join(srow1)+temp+' | '.join(row[:3]))
    print('---------'+temp+'---------')
    print(' | '.join(srow2)+temp+' | '.join(row[3:6]))
    print('---------'+temp+'---------')
    print(' | '.join(srow3)+temp+' | '.join(row[6:]))

def game_play():
    global play
    check_win()
    end = ''

    while play:
        point = input('\n{}'.format(who_playing(False)))
        if point == 'q'or point == 'Q':
            play = False
            print('\n GoodBye Quiter!!! \n')
            return
        while not validate_play(point):
            print('Invalid position try again!')
            point = input('\n{}'.format(who_playing(False)))
            if point == 'q'or point == 'Q':
                play = False
                print('\n GoodBye Quiter!!! \n')
                return
        place_player(point)
        who_playing(True)
        end = check_win()
        print_board(row,srow1,srow2,srow3)
    end_game(end)
        

def check_win():
    global play
    global row
    global locations
    play = True

    list_of_list = [row[:3],row[3:6],row[6:],row[1::3],row[2::3],row[3::3],row[::4],row[2::2]]
    
    for group in list_of_list:
        if len(group) == 3 and len(set(group)) == 1 and (list(set(group))[0] == 'X' or list(set(group))[0] == 'O'):
            print('hey')
            play = False
            return '\n                 {} wins                \n'.format(list(players.keys())[list(players.values()).index(group[0])])
    if len(locations) == 0:
        play = False
        return '\n                 Draw!!!                \n'
    else:
        return ''

def who_playing(switch):
    global playing
    ret = ['Player1\'s turn: ','Player2\'s turn: ']
    if switch:
        if playing == 0:
            playing = 1
            return 'Player1\'s turn: '
        else:
            playing = 0
            return 'Player2\'s turn: '
    else:
        return ret[playing]

def validate_play(locat):
    global locations

    if locat in locations:
        locations.remove(locat)
        return True
    else:
        return False

def place_player(locat):
    global row

    pos = int(locat) - 1

    row[pos] = players[players_list[playing]]

def end_game(game):
    if not game == '':
        print(game)
        temp = input('Rematch??? enter "Y" to play again or any key to quit: ')
        if temp == 'Y' or temp == 'y':
            start_game()
        else:
            print('\nWas fun having you... Goodbye :(\n')
        return
    else:
        pass


intro()
decide_start()