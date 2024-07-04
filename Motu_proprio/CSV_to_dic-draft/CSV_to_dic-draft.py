
from icecream import ic

def main():
    print()
    ic.disable()
    with open('right.csv', encoding='utf-8') as stream:
    # with open('right_bezBOM.csv', encoding='utf-8') as stream:
        content = stream.read()
    # print(content)
    
    
    start_range = 0
    
    ic(content[0])
    if content[0] == '\ufeff':
        ic('is BOM')
        start_range = 1
    ic(content)
    

    ic(content[0])
    ic(content[1])

    # print(content)
    ic(content)
    
    # Simple decomment
    #Jeżeli w linii przed pojawieniem się kratki pojawi się coś innego niż znak niedrukowalny, to taka linia nie będzie uwzględniona
    comment_mode = False
    else_mode = False
    len1 = len(content)
    decommented = ""
    
    for char in range(start_range, len1):
        if content[char] == '#':
            if else_mode:
                decommented += content[char]
            else:
                comment_mode = True
        elif content[char] == '\n':
            else_mode = False
            if comment_mode:
                comment_mode = False
            else:
                decommented += content[char]
        elif content[char].isspace():
            if comment_mode:
                pass
            else:
                decommented += content[char]
            pass
        else:
            if not comment_mode:
                else_mode = True
                decommented += content[char]
    
    content = decommented
    char_w = len1 = len(content)
    
    start_range = 0    
    for char in content:
        ic.disable()
        ic('in while - teraz to kolejne for')
        ic(start_range)
        ic(char)
        if char == '\"':
            break
        # elif char.isspace() or char == '\ufeff':
        elif char.isspace(): # or char == '\ufeff':
            start_range += 1
        else:
            ic('Zaraz wyłączy program')
            print('nieprawidłowy format csv. Przerwanie programu')
            exit()
        
        
    
        
    # ic.enable()    
    ic('przed for')
    ic(char, "przed for")  
    ic(start_range, "przed for")
    ic(type(char))
    ic(content)
    ic.disable()
    
    cache_str = ""
    cache_str_temp = ""
    column_quote_number = 0
    entries_dic = {}
    line_change   = False
    separation_checking = False
    comma_present = False
    quote_and_newline_occurence = False
    column_index = 0
    current_value_list = []
    
    # print('str - cache_str', 't - cache_str_temp', 'cv - current_value_list', 'c - char' , 'q - column_quote_number', 'ci - column_index', 'sep - separation_checking', sep='\n')
    
    for char in range(start_range, len1):
        # ic.enable()
        # print('c:', char, content[char], 'q:', column_quote_number, 'ci:', column_index, 'sep:', separation_checking, 'str:', cache_str, 't:', cache_str_temp, 'cv:', current_value_list)
        
        if content[char]=='\"':
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
                if column_index == 0:
                    entries_dic.update({cache_str : None})
                    current_key = cache_str
                else:
                    current_value_list.append(cache_str)
                column_index += 1
                cache_str = ""
                cache_str_temp = ""
                column_quote_number = 1 #mod
                separation_checking = False
            elif separation_checking and quote_and_newline_occurence:
                # line_change = True
                ic('\"+separation_checking+quote_and_newline_occurence')
                if column_index == 0:
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
                    ic(column_index)
                column_index = 0
                separation_checking = False
                comma_present = False
                cache_str = ""
                cache_str_temp = ""
                
            elif separation_checking:
                ic("\"+only separation checking")
                cache_str_temp += content[char]
            # elif column_index == 0:
            #     ic('elif column_index == 0:')
            #     cache_str = ""
            #     cache_str_temp = ""
            else:
                ic("\" + else")
                column_quote_number += 1
                separation_checking = True
                # if not line_change:
                cache_str_temp += content[char]
        elif content[char]==',':
            if separation_checking:
                cache_str_temp += content[char]
                comma_present = True
            else:
                cache_str += content[char]
                cache_str_temp += content[char]
                separation_checking = False
        elif content[char]=='\n':
            if line_change:
                pass
            elif separation_checking:
                ic("\\n+separation_checking")
                ic('Enter')
                if comma_present:
                    ic("Comma is present")
                    cache_str = cache_str_temp + content[char]
                    cache_str_temp += content[char]
                
                else:
                    quote_and_newline_occurence = True
                    cache_str_temp += content[char]
                # ic(cache_str, cache_str_temp)
                # ic(comma_present, quote_and_newline_occurence)
            else:
                cache_str += content[char]
                cache_str_temp += content[char]
                
        elif content[char].isspace() and not content[char]=='\n':
            if separation_checking:
                cache_str_temp += content[char]
            else:
                cache_str += content[char]
                cache_str_temp += content[char]
        else:
            if column_quote_number == 0:
                print('nieprawidłowy format csv. Przerwanie programu')
                exit()
            elif separation_checking:
                comma_present = False
                separation_checking = False
                line_change = False
                cache_str = cache_str_temp + content[char]
                cache_str_temp += content[char]
            else:
                cache_str += content[char]
                cache_str_temp += content[char]
        # ic(comma_present, cache_str, cache_str_temp)
        # ic(cache_str, cache_str_temp)
    
    # ic.enable()
    comma_present = False
    present_ending_quote = False
    checked_ending = False
    # Checking ending quote
    while not present_ending_quote and char_w >=0 :
        char_w -= 1
        if content[char_w]=='\"':
            present_ending_quote = True
        elif content[char_w].isspace() and not present_ending_quote:
            pass
        else:
            print('nieprawidłowy format csv. Przerwanie programu')
            exit()
    # Trzeba się jeszcze dalej cofać, aż sprawdzimy, że przed ostatnim cudzysłowem nie ma średnika lub znaku nowej linii
    ic.enable()
    ic("Czy tu wywala?")
    ic.disable()
    
    while not checked_ending and char_w >= 0:
        char_w -= 1
        if char_w == 0 and not content[char_w] == '\"':
            print('nieprawidłowy format csv. Przerwanie programu')
            exit()
        elif content[char_w] == ',' and not comma_present:
            comma_present = True
        elif comma_present and content[char_w] == '\"':
            print('nieprawidłowy format csv. Przerwanie programu')
            exit()
        elif content[char_w].isspace():
            pass
        else:
            checked_ending = True 
    
    
    if column_index == 0:
        entries_dic.update({cache_str : None})
    else:
        ic(current_value_list)
        current_value_list.append(cache_str)
        temp_tuple = tuple(current_value_list)
        ic(temp_tuple)
        entries_dic.update({current_key : temp_tuple})

    # 
    ic(current_value_list)
    ic(column_quote_number)
    ic(cache_str)
    ic(column_index)
    ic(line_change)
    print(entries_dic)
    ic.enable()
    ic(entries_dic)

    # Niedołączone dane mogą się znajdować w:
    # current_value_list
    # cache_str
    # cache_str_temp
    # Przypadek
    # 1. There is new line sign. 
    # ✅2. A new line was launched with a quotation mark 
    # 3. The introduction of characters into the new line has begun.
    # 4. The first columnt was completed.
    # 5. Second column was launched.
    # 6. Second column was completed
    #
    #
    # a. First of all, we will be going from the back.
    # We will be looking for quotation mark. Whitespace is accepted, anything else not. If anything except for quotation mark  or whitespace occurs. Program will be interrupted.

if __name__ == "__main__":
    main()
