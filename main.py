import pandas

# Create a dictionary in this format { 'A': 'Alpha', 'B': 'Beta', ...}

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet.to_dict()
phonetic_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter a word: ").upper()
output = [phonetic_dict[letter] for letter in name]
print(output)