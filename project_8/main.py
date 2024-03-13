# Ceaser Cypher encoder
from art import logo
from os import system

def ceaser(ceaser_direction: str, plain_text: str, shift_amount: int):
    end_text = ""

    if ceaser_direction == "decode":
        shift_amount *= -1

    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)

            new_position = position + shift_amount

            if new_position > 25 or new_position < 0:
                new_position %= 26

            end_text += alphabet[new_position]
        else:
             end_text += char

    print(f"The {ceaser_direction}d text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(direction, text, shift)

    choice = input("Do you want to keep using this software? type 'yes' or 'no': ")

    if choice == "no":
         should_continue = False
    else:
        system("clear")

print("Goodbye and thank you for using our software!")
