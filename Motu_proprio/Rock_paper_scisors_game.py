# Rock, paper, scissors

# import getpass
# Pobranie hasła od użytkownika bez wyświetlania wpisywanego tekstu
# password = getpass.getpass("Enter your password: ")
# print("Your password has been entered.")
import pwinput
import random
from icecream import ic

two_player_mode = bool( 0 )

# Choose program engine: 1-4
# print( '''Choose program engine: \n
#     1 - list_of_elifs \n
#     2 - list_of_elifs \n 
#     3 - dic_plus_tuple \n
#     4 - modulo_mode'''
#     )
program_engine = 2

def f_1_player_mode():
    if not two_player_mode:
        var_range = 1
        print('Your opponent is computer.')
        input_matrix[1][1] = random.choice(list(input_dict))
    else:
        var_range = len(input_matrix)
        
    for i in range(var_range):
        
        input_matrix[i][1] = pwinput.pwinput(input_matrix[i][0] + ': ')
        if input_matrix[i][1] not in input_dict:
            print('Entered string:', input_matrix[i][1])
            print('Incorrect input. Pogramm interrupted')
            exit()
    print()

def f_2_player_mode():
    for i in range(len(input_matrix)):
        input_matrix[i][1] = pwinput.pwinput(input_matrix[i][0] + ': ')
        if input_matrix[i][1] not in input_dict:
            print('Entered string:', input_matrix[i][1])
            print('Incorrect input. Pogramm interrupted')
            exit()
    print()

def list_of_elifs():
    if input_matrix[0][1] == 'r' and input_matrix[1][1] == 's':
        print('You win!')
    elif input_matrix[0][1] == 'r' and input_matrix[1][1] == 'p':
        print('You loose!')
    elif input_matrix[0][1] == 'r' and input_matrix[1][1] == 'r':
        print('Draw!')
    elif input_matrix[0][1] == 'p' and input_matrix[1][1] == 'r':
        print('You win!')
    elif input_matrix[0][1] == 'p' and input_matrix[1][1] == 's':
        print('You loose!')
    elif input_matrix[0][1] == 'p' and input_matrix[1][1] == 'p':
        print('Draw!')
    elif input_matrix[0][1] == 's' and input_matrix[1][1] == 'p':
        print('You win!')
    elif input_matrix[0][1] == 's' and input_matrix[1][1] == 'r':
        print('You loose!')
    elif input_matrix[0][1] == 's' and input_matrix[0][1] == 's':
        print('Draw!')

def ifs_tree():
    if input_matrix[0][1] == 'r':
        if input_matrix[1][1] == 's':
            print('You win!')
        elif input_matrix[1][1] == 'p':
            print('You loose!')
        elif input_matrix[1][1] == 'r':
            print('Draw!')
    elif input_matrix[0][1] == 'p':
        if input_matrix[1][1] == 'r':
            print('You win!')
        elif input_matrix[1][1] == 's':
            print('You loose!')
        elif input_matrix[1][1] == 'p':
            print('Draw!')
    elif input_matrix[0][1] == 's':
        if input_matrix[1][1] == 'p':
            print('You win!')
        elif input_matrix[1][1] == 'r':
            print('You loose!')
        elif input_matrix[0][1] == 's':
            print('Draw!')

def dic_plus_tuple(player1, player2):    
    results_dic = {
        ('r', 'r'): results_out_dic['draw'],
        ('r', 'p'): results_out_dic['defeat'],
        ('r', 's'): results_out_dic['win'],
        ('p', 'r'): results_out_dic['win'],
        ('p', 'p'): results_out_dic['draw'],
        ('p', 's'): results_out_dic['defeat'],
        ('s', 'r'): results_out_dic['defeat'],
        ('s', 'p'): results_out_dic['win'],
        ('s', 's'): results_out_dic['draw']        
    }
    print(results_dic[(player1, player2)])


def modulo_mode(player1, player2):
    value_map_dic = {
        'r' : 0,
        'p' : 1,
        's' : 2
    }
    if player1 == player2:
        print(results_out_dic['draw'])
    elif ((value_map_dic[player1] - value_map_dic[player2]) % 3) == 1:
        print(results_out_dic['win'])
    else:
        print(results_out_dic['defeat'])

input_matrix = [
    ['Your turn', 'a'],
    ['Opponent turn', 'b']
]

# Tworzenie słownika z początkowymi wartościami
input_dict = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

results_out_dic = {
        'win' : 'You win! Opponent loose!',
        'defeat' : 'You loose! Opponent win!',
        'draw' : 'Draw!' 
    }


print('\n' + 'Rock paper scissors.' +  '\n')
print('As input enter one of three letters:')
print('“r” stands for “rock”,')
print('“p” stands for “paper”,')
print('“s” stands for “scissors”.' +  '\n')


f_1_player_mode()

for i in range(len(input_matrix)):
    print(input_matrix[i][0] + ':', input_dict[input_matrix[i][1]])
print()

functions_dic = {
    1 : (list_of_elifs, ()),
    2 : (ifs_tree, ()),
    3 : (dic_plus_tuple, (input_matrix[0][1], input_matrix[1][1])),
    4 : (modulo_mode, (input_matrix[0][1], input_matrix[1][1]))
}

function_, args_ = functions_dic[program_engine]
function_(*args_)
function_n = function_.__name__

print(3*'\n' + 'Proudly powered by:', function_n )