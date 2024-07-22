# Bonusowe minićwiczenia:

# 1. Napisz program, który zlicza ile jest słów w pliku tekstowym.
from icecream import ic
import CSV_to_dic02

def language_choice():
    language = input('\n'+'Press „Enter” to keep the program interface in English albo wpisz „pl” i naciśnij “Enter”, aby ustawić język interfesju na język polski.: ')
    if language == "pl":
        return 1
    else:
        return 0

def ext_dic(d_key, d_lang):
    i18n_dic_e ={}
    try:
        i18n_dic_e = CSV_to_dic02.main('i18n_en_pl.csv', d_lang)
    # except CSV_to_dic02.StructureErrorException:
    #     pass
    except:
        return d_key
    return i18n_dic_e[d_key][d_lang]

def main():
    lang = language_choice()
    print('\n'+ ext_dic("presentation", lang)+ "." + "\n")
    path = input( ext_dic("prompt",lang)+": ")
    # path = 'zyciemozebyc.txt'
    try:
        with open(path) as stream:
            content = stream.read()
            # implicit stream.close()
    except:
        try:
            with open(path, encoding='utf-8') as stream:
                content = stream.read()
        except:
            print("\n"+ ext_dic("read_err",lang)+".", ext_dic("presentation",lang)+".")
            exit()
    words_number = len(content.split())
    print("\n"+ ext_dic("number_of_words",lang)+":", words_number)

if __name__ == "__main__":
    main()
