from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    try:
        website = entry_website.get().lower()
        with open("data.json", "r") as data_file:
            try:
                data = json.load(data_file)
                website_data = data[website]
                login = website_data["login"]
                password = website_data["password"]
                messagebox.showinfo(title=f"{website.title()}", message=f"Login: {login}\n"
                                                                        f"Password: {password}")
            except KeyError:
                messagebox.showinfo(title=f"Error", message=f"No details for website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message=f"No Data File Found.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get().lower()
    login = entry_email.get().lower()
    password = entry_password.get().lower()
    new_data = {website: {
        "login": login,
        "password": password
    }}

    if website == "" or login == "" or password == "":
        messagebox.showinfo(title="Empty Field", message="Please don't leave any field empty!")
    else:
        save_password = messagebox.askyesno(title="Save Password",
                                            message=f"Would you like to save the {website.title()} password?")
        if save_password:
            try:
                with open("data.json", "r") as data_file:  # Reading json
                    json_info = json.load(data_file)
                    json_info.update(new_data)  # Uploading json
                with open("data.json", "w") as data_file:  # Writing updated json
                    json.dump(json_info, data_file, indent=4)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            messagebox.showinfo(title="Saved Password",
                                message=f"{website.title()} Password saved.")
            entry_website.delete(0, END)
            entry_email.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=15, pady=20)

canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=27)
entry_website.grid(column=1, row=1)
entry_website.focus()
entry_email = Entry(width=45)
entry_email.grid(column=1, row=2, columnspan=2)
entry_password = Entry(width=27)
entry_password.grid(column=1, row=3)

# Add button
search_password = Button(text="Search", width=14, command=find_password)
search_password.grid(column=2, row=1)

button_password = Button(text="Generate Password", width=14, command=generate_password)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=43, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
