import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_alphabet = {
    row.letter: row.code
    for _, row in data.iterrows()
}

user_word = input("Enter a word: ").upper()

word_spelling = [
    nato_alphabet.get(letter)
    for letter in user_word if letter != " "
]

print(word_spelling)
