
from icecream import ic

def start_range_ref_to_BOM(content_f1):
    start_range_f1 = 0
    # ic(content_f1[0])
    if content_f1[0] == '\ufeff':
        # ic('is BOM')
        start_range_f1 = 1
    # ic(content_f1)
    return start_range_f1

def decommenting(start_range_f1, content_f2):
    # Simple decomment
    #Jeżeli w linii przed pojawieniem się kratki pojawi się coś innego niż znak niedrukowalny, to taka linia nie będzie uwzględniona
    else_mode = False
    decommented = ""
    comment_mode = False
    len_f2 = len(content_f2)
    for char in range(start_range_f1, len_f2):
        if content_f2[char] == '#':
            if else_mode:
                decommented += content_f2[char]
            else:
                comment_mode = True
        elif content_f2[char] == '\n':
            else_mode = False
            if comment_mode:
                comment_mode = False
            else:
                decommented += content_f2[char]
        elif content_f2[char].isspace():
            if comment_mode:
                pass
            else:
                decommented += content_f2[char]
            pass
        else:
            if not comment_mode:
                else_mode = True
                decommented += content_f2[char]
    return decommented

def do_quote_is_at_the_beginning(content_f3):
#do_quote_is_at_the_beginning
    start_range_f3 = 0    
    for char in content_f3:
        # ic.disable()
        # ic('in while - teraz to kolejne for')
        # ic(start_range)
        # ic(char)
        if char == '\"':
            break
        # elif char.isspace() or char == '\ufeff':
        elif char.isspace(): # or char == '\ufeff':
            start_range_f3 += 1
        else:
            ic('Zaraz wyłączy program')
            print('nieprawidłowy format csv. Przerwanie programu')
            exit()
    return start_range_f3

def main_work(start_range_f4, content_f4):
    len_f4 = len(content_f4)
    cache_str = "" # needed outside
    cache_str_temp = ""
    column_quote_number = 0
    entries_dic = {} # needed as output
    line_change   = False
    separation_checking = False
    comma_present = False
    quote_and_newline_occurence = False
    column_index_f4 = 0 # needed outside
    current_value_list = [] # needed outsie
    print('str - cache_str', 't - cache_str_temp', 'cv - current_value_list', 'c - char' , 'q - column_quote_number', 'ci - column_index', 'sep - separation_checking', sep='\n')
    for char in range(start_range_f4, len_f4):
        # ic.enable()
        print('c:', char, content_f4[char], 'q:', column_quote_number, 'ci:', column_index_f4, 'sep:', separation_checking, 'str:', cache_str, 't:', cache_str_temp, 'cv:', current_value_list)    
        if content_f4[char]=='\"':
            # ic("\"")
            if column_quote_number == 0 :
                # ic("if")
                ic()
                column_quote_number += 1
                # a = b + c 
                # column_quote_number = column_quote_number + 1
            elif separation_checking and comma_present:
                # print(f"{current_value_list= }")
                ic('elif comma_present')
                comma_present = False
                # To znaczy, że mieniamy kolumnę
                if column_index_f4 == 0:
                    entries_dic.update({cache_str : None})
                    current_key = cache_str
                else:
                    current_value_list.append(cache_str)
                column_index_f4 += 1
                cache_str = ""
                cache_str_temp = ""
                column_quote_number = 1 #mod
                separation_checking = False
            elif separation_checking and quote_and_newline_occurence:
                # line_change = True
                ic('\"+separation_checking+quote_and_newline_occurence')
                if column_index_f4 == 0:
                    entries_dic.update({cache_str : None})
                    current_key = cache_str
                else:
                    current_value_list.append(cache_str)
                    ic(current_value_list)
                    temp_tuple = tuple(current_value_list)
                    current_value_list = []
                    ic(current_key)
                    entries_dic.update({current_key : temp_tuple})
                    ic(entries_dic)
                    ic(column_index_f4)
                column_index_f4 = 0
                separation_checking = False
                comma_present = False
                cache_str = ""
                cache_str_temp = ""
                
            elif separation_checking:
                ic("\"+only separation checking")
                cache_str_temp += content_f4[char]
            else:
                ic("\" + else")
                column_quote_number += 1
                separation_checking = True
                # if not line_change:
                cache_str_temp += content_f4[char]
        elif content_f4[char]==',':
            if separation_checking:
                cache_str_temp += content_f4[char]
                comma_present = True
            else:
                cache_str += content_f4[char]
                cache_str_temp += content_f4[char]
                separation_checking = False
        elif content_f4[char]=='\n':
            if line_change:
                pass
            elif separation_checking:
                ic("\\n+separation_checking")
                ic('Enter')
                if comma_present:
                    ic("Comma is present")
                    cache_str = cache_str_temp + content_f4[char]
                    cache_str_temp += content_f4[char]
                else:
                    quote_and_newline_occurence = True
                    cache_str_temp += content_f4[char]
                # ic(cache_str, cache_str_temp)
                # ic(comma_present, quote_and_newline_occurence)
            else:
                cache_str += content_f4[char]
                cache_str_temp += content_f4[char]
                
        elif content_f4[char].isspace() and not content_f4[char]=='\n':
            if separation_checking:
                cache_str_temp += content_f4[char]
            else:
                cache_str += content_f4[char]
                cache_str_temp += content_f4[char]
        else:
            if column_quote_number == 0:
                print('nieprawidłowy format csv. Przerwanie programu')
                exit()
            elif separation_checking:
                comma_present = False
                separation_checking = False
                line_change = False
                cache_str = cache_str_temp + content_f4[char]
                cache_str_temp += content_f4[char]
            else:
                cache_str += content_f4[char]
                cache_str_temp += content_f4[char]
        # ic(comma_present, cache_str, cache_str_temp)
        # ic(cache_str, cache_str_temp)
        
    #Zapisywanie ostatnich wartości
    if column_index_f4 == 0:
        entries_dic.update({cache_str : None})
    else:
        # ic(current_value_list)
        current_value_list.append(cache_str)
        temp_tuple = tuple(current_value_list)
        # ic(temp_tuple)
        entries_dic.update({current_key : temp_tuple})
    # return cache_str, current_value_list, entries_dic, column_index_f4, current_key
    return entries_dic

def end_consistency_check(content_f5):
    # a. First of all, we will be going from the back.
    # We will be looking for quotation mark. Whitespace is accepted, anything else not. If anything except for quotation mark  or whitespace occurs. Program will be interrupted.
    # Checking ending quote
    char_w = len(content_f5)
    present_ending_quote = False
    while not present_ending_quote and char_w >=0 :
        char_w -= 1
        if content_f5[char_w]=='\"':
            present_ending_quote = True
        elif content_f5[char_w].isspace() and not present_ending_quote:
            pass
        else:
            print('nieprawidłowy format csv. Przerwanie programu')
            exit()
    # Trzeba się jeszcze dalej cofać, aż sprawdzimy, że przed ostatnim cudzysłowem nie ma średnika lub znaku nowej linii    
    checked_ending = False
    comma_present = False
    while not checked_ending and char_w >= 0:
        char_w -= 1
        if char_w == 0 and not content_f5[char_w] == '\"':
            print('nieprawidłowy format csv. Przerwanie programu')
            exit()
        elif content_f5[char_w] == ',' and not comma_present:
            comma_present = True
        elif comma_present and content_f5[char_w] == '\"':
            print('nieprawidłowy format csv. Przerwanie programu')
            exit()
        elif content_f5[char_w].isspace():
            pass
        else:
            checked_ending = True 
    
def main():
    print()
    # ic.disable()
    with open('right_t1.csv', encoding='utf-8') as stream:
    # with open('right.csv', encoding='utf-8') as stream:
    # with open('right_bezBOM.csv', encoding='utf-8') as stream:
        content = stream.read()
    # print(content)
    
    start_range = start_range_ref_to_BOM(content)
    content = decommenting(start_range, content)
    start_range = do_quote_is_at_the_beginning(content)
    end_consistency_check(content)
    # cache_str_out, values_list, dic_out, column_index, c_key = main_work(start_range, content)
    dic_out = main_work(start_range, content)
    
    print(dic_out)
    ic(dic_out)

    # Niedołączone dane mogą się znajdować w:
    #
    # Przypadek
    # 1. There is new line sign. 
    # ✅2. A new line was launched with a quotation mark 
    # 3. The introduction of characters into the new line has begun.
    # 4. The first columnt was completed.
    # 5. Second column was launched.
    # 6. Second column was completed
    #
    #
    
if __name__ == "__main__":
    main()
