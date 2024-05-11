# Vicious_loop_one_char.py
# ... for sad path
# One character - Vicious loop for sad path
#
statement = "I do not mean to follow your prompt."
# character = "begin"
character = input("\nPlease enter one character, it will be checked if it is a letter or not: ")
# length_ = 0
while (len(character) != 1):
    if character == statement:
        break
    character = input('\nOnce more please, enter one character, that will be checked if it is a letter or not. Alternatively you can type : "I do not mean to follow your prompt." to stop program: ')

if len(character) == 1 :
    if character.isalpha():
        print('Character "', character, '" is a letter.', sep="")
    else:
        print('\n', 'Entered character "', character, '" is not a letter.', sep="")