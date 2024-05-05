# M01L13c_BBC_project.py

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.
#-----------------------------------
# Show average word length.

text = input("Paste below please text that is going to be calculated for avareage word length:\n")

words_table = text.split()
number_of_words = len(words_table)
text_length = len(text)

number_of_characters_without_spaces = text_length - (number_of_words - 1)
average_word_length = number_of_characters_without_spaces / number_of_words
print("Number of words:", number_of_words)
print("Average word length:", average_word_length)