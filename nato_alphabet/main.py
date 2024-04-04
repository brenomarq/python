import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_alphabet = {
    row.letter: row.code
    for _, row in data.iterrows()
}

while True:
    user_word = input("Enter a word: ").upper()

    try:
        word_spelling = [
            nato_alphabet[letter]
            for letter in user_word if letter != " "
        ]

    except KeyError:
        print("Sorry, only letters are accepted.")

    else:
        print(word_spelling)
        break
