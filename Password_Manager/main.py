from tkinter import *
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = list(charact_entry.get())

    password_letters_lower = [choice(letters_lower) for char in range(var_total_char.get())]

    if var_upper.get() == 1:
        password_letters_upper = [choice(letters_upper) for char in range(randint(10, 20))]
    else:
        password_letters_upper = []

    if var_number.get() == 1:
        password_numbers = [choice(numbers) for char in range(randint(6, 8))]
    else:
        password_numbers = []

    if var_caract.get() == 1:
        password_symbols = [choice(symbols) for char in range(randint(4, 6))]
    else:
        password_symbols = []

    password_list = password_letters_upper + password_letters_lower + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list[0:var_total_char.get()])
    label_password.config(text=password)


# ---------------------------- COPY FUNCTION ------------------------------- #
def copy_password():
    pyperclip.copy(label_password.cget("text"))

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=20)
window.minsize(width=400, height=380)
window.maxsize(width=400, height=380)

canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

#  Labels
label_password = Label(text=";66r3gWaM~", padx=15, font=("arial", 20, "normal"))
label_password.grid(column=1, row=1)

# buttons
copy_password = Button(text="Copiar", command=copy_password)
copy_password.grid(column=2, row=1)

restart_password = Button(text="Gerar", command=generate_password)
restart_password.grid(column=2, row=3)

# options
var_total_char = IntVar()
var_total_char.set(15)
total_char = Spinbox(from_=8, to=20, width=5, textvariable=var_total_char)
total_char.grid(column=0, row=2)

var_upper = IntVar()
az_button = Checkbutton(text="A-Z", variable=var_upper)
az_button.select()
az_button.grid(column=0, row=3)

var_number = IntVar()
numbers_button = Checkbutton(text="0-9", variable=var_number)
numbers_button.select()
numbers_button.grid(column=0, row=4)

var_caract = IntVar()
charact_button = Checkbutton(variable=var_caract)
charact_button.select()
charact_button.grid(column=0, row=5)

charact_entry = Entry(width=30)
charact_entry.insert(0, "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
charact_entry.grid(column=1, row=5)

window.mainloop()
