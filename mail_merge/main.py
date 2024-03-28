#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as file:
    names_from_file = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

# Removes the newline from the strings
names = [
    names_from_file[i].strip()
    for i in range(len(names_from_file))
]

# Write a letter for each person
for name in names:
    formatted_letter = starting_letter.replace("[name]", name)

    with open(f"./Output/ReadyToSend/letter_for_{name.lower()}.txt", "w+") as file:
        file.write(formatted_letter)
