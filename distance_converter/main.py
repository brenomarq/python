import tkinter as tk
FONT = ("Arial", 12, "bold")

def convert() -> None:
    value = int(miles_entry.get())
    new_value = value * 1.609

    kilometers.config(text=f"miles = {new_value:.2f} km")


window = tk.Tk()
window.title("Distance converter")
window.minsize(width=300, height=150)

title = tk.Label(text="Convert:", font=FONT)
title.grid(column=0, row=0, pady=5)

miles_entry = tk.Entry(width=10)
miles_entry.grid(column=0, row=1)
miles_entry.focus()

kilometers = tk.Label(text="miles = ... km", font=FONT)
kilometers.grid(column=1, row=1)

calculate_button = tk.Button(text="Calculate", command=convert)
calculate_button.grid(column=0, row=2, pady=20)

window.mainloop()
