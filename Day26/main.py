import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dataframe = pandas.DataFrame(data)
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("What word do you want to convert phonetically? ").upper()

user_word_converted = [phonetic_dict[letter] for letter in user_word]

print(user_word_converted)
