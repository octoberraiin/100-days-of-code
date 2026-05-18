import pandas

alphabets_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabets_dict = {row.letter: row.code for (index, row) in alphabets_df.iterrows()}


user_word = input("Enter a word: ").upper()
code_words = [alphabets_dict[letter] for letter in user_word]
print(code_words)
