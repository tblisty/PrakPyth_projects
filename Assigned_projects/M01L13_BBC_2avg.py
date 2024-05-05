# M01L13c_BBC_project.py

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.
#-----------------------------------
# Begin of the program

# Text simplicity estimation.

# What program should have to do?
# 1. Show average word length.
# 2. Count average number of words in sentence.

print()
print("Text simplicity estimation.\n")

# Built-in sample text
text = "Ala ma kota. Kot lubi Alę. Lecz mama Ali nie lubi go wcale. Mówi, że sierściuch. Że pchły roznosi. Że co dzień nad ranem myszy przynosi. I żre się Ala ze swoją mamą, że kot głośno miauczy codziennie rano. A tata zaciera z uśmiechem swe ręce. To on przyniósł Ali kota w prezencie. Znalazł go gdzieś tam. Pewnego razu. Przy starym śmietniku. Obok garażu. Ujął go wdziękiem. I kocim chodem. Zlitował się tata. Nad kocim głodem. I siedzi nasz kotek. W oku cyklonu. Słuchając awantur. Po kątach domu. I myśli sobie. Nieszczęsny kotek: Po jaką cholerę właziłem na płotek?"

# Paste here please text that is going to be estimated for its simplicity
text = input("Paste below please text that is going to be estimated for its simplicity:\n")

words_table = text.split()
number_of_words = len(words_table)
text_length = len(text)

# Average word length
number_of_characters_without_spaces = text_length - (number_of_words - 1)
average_word_length = number_of_characters_without_spaces / number_of_words
print("\nNumber of words: ", number_of_words, ".", sep="")
print("Average word length:", average_word_length, "characters.")
    
# Average sentence length
number_of_sentences = 0
for n in range(text_length):
    if (text[n] == "." or text[n] == "?" or text[n] == "!") and (n < text_length - 3) and (text[n + 1] == " ") and (text[n + 2].isupper() == True):
        number_of_sentences += 1
    elif (text[n] == "." or text[n] == "?" or text[n] == "!") and (n >= text_length - 3):
        number_of_sentences += 1
        n = text_length - 1
     
average_sentence_length = number_of_words / number_of_sentences
print("Number of sentences: ", number_of_sentences, ".", sep="")
print("Average sentence length:", average_sentence_length, "words.")