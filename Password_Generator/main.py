import string
from tkinter import *
from random import randint, choice, shuffle
from tkinter import messagebox
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
        try:
            password_symbols = [choice(symbols) for char in range(randint(4, 6))]
        except IndexError:
            messagebox.showinfo(title=f"Erro", message="Campo de caracteres especiais vazio.")
    else:
        password_symbols = []

    password_list = password_letters_upper + password_letters_lower + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list[0:var_total_char.get()])
    label_password.config(text=password)


# ---------------------------- COPY FUNCTION ------------------------------- #
def copy_password():
    pyperclip.copy(label_password.cget("text"))

# ---------------------------- SPECIAL CHARACTERS VALIDATION ------------------------------- #
# def special_char_validation():
#     print(var_charact_entry)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(pady=20)
window.minsize(width=400, height=380)
window.maxsize(width=400, height=380)

title = LabelFrame(width=380, height=340)
title.place(x=10, y=10)

canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.place(x=100, y=12)

#  Labels
label_password = Label(text=";7%lP[Ezm7Eu2ltN~x4SD", padx=15, font=("arial", 17, "normal"))
label_password.place(x=12, y=210)

# buttons
copy_password = Button(text="Copiar", command=copy_password)
copy_password.place(x=334, y=214)

restart_password = Button(text="Gerar", command=generate_password)
restart_password.place(x=338, y=244)

# options
var_total_char = IntVar()
var_total_char.set(16)
total_char = Spinbox(from_=6, to=20, width=3, textvariable=var_total_char)
total_char.place(x=30, y=264)
password_lenght = Label(text="Comprimento da Senha")
password_lenght.place(x=65, y=262)

var_upper = IntVar()
az_button = Checkbutton(text="A-Z", variable=var_upper)
az_button.select()
az_button.place(x=24, y=294)

var_number = IntVar()
numbers_button = Checkbutton(text="0-9", variable=var_number)
numbers_button.select()
numbers_button.place(x=84, y=294)

var_caract = IntVar()
charact_button = Checkbutton(variable=var_caract)
charact_button.select()
charact_button.place(x=144, y=294)

var_charact_entry = StringVar()
charact_entry = Entry(width=30, validate="focusout")
charact_entry.insert(0, "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
charact_entry.place(x=170, y=297)

window.mainloop()