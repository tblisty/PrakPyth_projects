# M03L07f_sum_with_ext_i18n.py

# from icecream import ic
from M03L07fa_sum_i18n import dic_get

def string_to_number( f_string ):
    work_string = ''
    # ic(f_string)
    comma_not_present = True
    char = 0
    while char < len(f_string):
        are_letters = False == (f_string[char].isdigit() or f_string[char] == ',' or f_string[char] == '.' or f_string[char].isspace() or f_string[0] == '-')
        if f_string[char].isdigit():
            work_string += f_string[char]
        elif (f_string[char] == ',' or f_string[char] == '.') and comma_not_present:
            work_string += '.'
            comma_not_present = False
        elif are_letters:
            char = len(f_string)
        elif f_string[0] == '-':
            work_string += '-'
        char += 1
    try:
        return int(work_string)
    except:
        return float(work_string)

def main():
    i18n = input('\n'+'For english type "en" and press "Enter" lub po prostu wciśnij "Enter", by pozostawić interfej w języku polskim: ')
    if i18n == "en":
        i18n = 0
    else:
        i18n = 1

    print('\n'+dic_get("progr", i18n), '\n')
    addend_a = input(dic_get("in_a", i18n) + ': ')
    addend_b = input(dic_get("in_b", i18n) + ': ')
    try:
        addend_a = string_to_number(addend_a)
        addend_b = string_to_number(addend_b)
    except:
        print(dic_get('conv_err', i18n)+'.', dic_get('p_exit', i18n)+'.')
        exit()

    sum_ = addend_a + addend_b
    print(dic_get('sum', i18n) + ':', sum_)



if __name__ == "__main__":
    main()

# Precedence and Associativity of Operators in Python
# Last Updated : 01 Jul, 2023
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | Precedence | Operators                                    | Description                                                 | Associativity |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 1          | ()                                           | Parentheses                                                 | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 2          | x[index], x[index:index]                     | Subscription, slicing                                       | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 3          | await x                                      | Await expression                                            | N/A           |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 4          | **                                           | Exponentiation                                              | Right to left |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 5          | +x, -x, ~x                                   | Positive, negative, bitwise NOT                             | Right to left |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 6          | *, @, /, //, %                               | Multiplication, matrix, division, floor division, remainder | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 7          | +, –                                         | Addition and subtraction                                    | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 8          | <<, >>                                       | Shifts                                                      | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 9          | &                                            | Bitwise AND                                                 | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 10         | ^                                            | Bitwise XOR                                                 | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 11         | |                                            | Bitwise OR                                                  | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 12         | in, not in, is, is not, <, <=, >, >=, !=, == | Comparisons, membership tests, identity tests               | Left to Right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 13         | not x                                        | Boolean NOT                                                 | Right to left |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 14         | and                                          | Boolean AND                                                 | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 15         | or                                           | Boolean OR                                                  | Left to right |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 16         | if-else                                      | Conditional expression                                      | Right to left |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 17         | lambda                                       | Lambda expression                                           | N/A           |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+
# | 18         | :=                                           | Assignment expression (walrus operator)                     | Right to left |
# +------------+----------------------------------------------+-------------------------------------------------------------+---------------+