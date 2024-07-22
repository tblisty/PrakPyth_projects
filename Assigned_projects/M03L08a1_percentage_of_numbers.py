### 🔴 Ćwiczenie

# Napisz program, który ocenia jak bardzo "naukowo" brzmi dany tekst. W tym celu policz jak często w tym zdaniu pojawiają się liczby. Wyświetl jaki procent wszystkich "słów" to właśnie liczby.
# Postaraj się, aby program nie zwracał uwagi na interpunkcję. To znaczy, że w zdaniu "Numer 1234." drugie słowo to "1234.". Potraktuj je jako liczbę, pomimo że zawiera kropkę.
# To oznacza, że zdefiniujesz stałą zawierającą kilka znaków interpunkcyjnych.
# Samodzielnie znajdź metodę do określania, czy dany string jest liczbą.

# from icecream import ic

TO_BE_REPLACED = ",./~!#$%^*()-+="

# Built_in example text
EXAMPLE_TEXT = '''STES 2024
W Marinie Yacht Park w Gdyni w dniu 24 czerwca 2024 r. odby Ships Races 2024, które wystartowały 27 czerwca 2024 r. w Kłajpedzie. Sama jednostka wyposażona w nowe Szczecinie 5 sierpnia 2024 r.

Konfere świetna sposobność, by podkreślić Jubileusz 20-lecia wejścia Polski do Unii Europejskiej.

Dodatkowo, wypłynięcie jednostki stanowi część obchodów 100-lecia 

KLAIPĖDA – Lithuania 27.06.2024 – 30.06.2024

HELSINKI – Finland 4.07.2024 – 7.07.2024

TALLINN – Estonia 11.07.2024 – 14.07.2024

TURKU – Finland 18.07.2024 – 21.07.2024

MARIEHAMN – Åland Islands 24.07.2024 – 27.07.2024

SZCZECIN – Polska 2.08.2024 – 5.08.2024
Casc'''

def main():
    # ic.disable()
    print('\n'+ "A programme that calculates the percentage of numbers among all the words in an input text" + "\n")
    # Program obliczający procentowy udział liczb wśród wszystkich słów we wprowadzonym tekście
    
    input_text = input('Enter your text and confirm pressing "Enter": ')
    # Wprowadź tekst i potwierdź naciskając „Enter”
    
    while input_text == "":
        input_text = input('You have not entered any character. Please, input any text and press “Enter”: ')
        # Nie wprowadzono żadnego znaku. Wprowadź dowolny tekst i naciśnij „Enter”.
    print()
    
    # Example text
    # input_text = EXAMPLE_TEXT
    
    words_list = input_text.split()
    number_of_words = len(words_list)
    no_punctation_list = []
    number_of_numbers = 0
    for word in words_list:
        for char in TO_BE_REPLACED:
            word = word.replace(char, "")
        no_punctation_list.append(word)
        if word.isnumeric():
            number_of_numbers += 1
    percentage_of_numbers = number_of_numbers * 100 / number_of_words
    print("percentage_of_numbers:", f"{percentage_of_numbers:.2f}")

if __name__ == "__main__":
    main()
