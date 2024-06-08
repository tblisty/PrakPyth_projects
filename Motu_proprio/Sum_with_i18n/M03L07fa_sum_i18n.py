# Internationalization file for M03L07f_sum_with_ext_i18n.py
# First column in dictionary: english
# Second column in dictionary: polish

def dic_get( key, i18n ):
    dic = {
    'progr': ('Programm summing two numbers', 'Program sumujący dwie liczby'),
    'lang' : ('language',                     'język'),
    'inp'  : ('input',                        'wejście'),
    'out'  : ('output',                       'wyjście'),
    'in_a' : ('Enter first number',           'Wprowadź pierwszą liczbę'), #term, addend
    'in_b' : ('Enter second number',          'Wrowadź drugą liczbę'),
    'sum'  : ('The sum of given numbers is',  'Suma podanych liczb wynosi'),
    'conv_err':('Cannot read entered data',   'Nie można odczytać wprowadzonych danych'),
    'p_exit':('Program interruption',         'Przerwanie programu')
    }
    return dic[key][i18n]

# if __name__ == "__main__":
    # main()
