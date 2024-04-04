import json
import pyperclip
import tkinter as tk
from random import choice, shuffle, randint
from tkinter import messagebox

BGCOLOR = "white"
DATA_FILE = "./data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password() -> None:
    """Generates a random password."""
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password = password_letters + password_symbols + password_numbers

    shuffle(password)

    new_password = "".join(password)

    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save() -> None:
    """Save the entries given by the user in a data file."""

    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open(DATA_FILE, "r") as file:
                data: dict = json.load(file)

        except FileNotFoundError:
            with open(DATA_FILE, "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open(DATA_FILE, "w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


def find_password() -> None:
    website = website_entry.get()

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        website_info = data[website]

    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File could be found.")

    except KeyError:
        messagebox.showerror(title="Oops", message="No details available for the website.")

    else:
        messagebox.showinfo(
            title=f"{website} information",
            message=f"Here's your information:\nEmail: {website_info['email']}\nPassword: {website_info['password']}"
        )
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, bg=BGCOLOR)
window.minsize(width=400, height=400)

canvas = tk.Canvas(width=200, height=200, bg=BGCOLOR, highlightthickness=0)
logo_img = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website: ", bg=BGCOLOR)
website_label.grid(row=1, column=0)
website_label.focus()

email_label = tk.Label(text="Email/Username: ", bg=BGCOLOR)
email_label.grid(row=2, column=0)

password_label = tk.Label(text="Password: ", bg=BGCOLOR)
password_label.grid(row=3, column=0)

website_entry = tk.Entry(width=31)
website_entry.grid(row=1, column=1, pady=3)

email_entry = tk.Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2, pady=3)
email_entry.insert(0, "personalemail@gmail.com")

password_entry = tk.Entry(width=31)
password_entry.grid(row=3, column=1)

search_btn = tk.Button(text="Search", command=find_password, width=14, padx=2)
search_btn.grid(row=1, column=2)

gpassword_btn = tk.Button(text="Generate Password", command=generate_password, padx=2)
gpassword_btn.grid(row=3, column=2)

add_pw_btn = tk.Button(text="Add", command=save, width=43)
add_pw_btn.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
