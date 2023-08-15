import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()
root.title("🔑")
root.minsize(width=360, height=450)
# root.config(padx=10)
style = ttk.Style("darkly")

title_text = ttk.Label(text="🔑 Gerador de Senhas", bootstyle="secondary")
title_text.grid(column=0, row=0, sticky=W, padx=10, pady=5, columnspan=5)

password = ttk.Label(text="Hu&*6b%Lk(H32", font=("TkDefaultFont", 20, "bold"))
password.grid(column=0, row=1, columnspan=5, padx=10)

copy_button = ttk.Button(text="💾", bootstyle="info")
copy_button.grid(column=6, row=1, padx=8)

repeat_button = ttk.Button(text="🔁")
repeat_button.grid(column=7, row=1, padx=2)

AZ_checkbutton = ttk.Checkbutton(text="A-Z")
AZ_checkbutton.grid(column=0, row=3, padx=25, sticky=W)

az_checkbutton = ttk.Checkbutton(text="az")
az_checkbutton.grid(column=1, row=3, sticky=W)

number_checkbutton = ttk.Checkbutton(text="0-9")
number_checkbutton.grid(column=2, row=3, sticky=W)

root.mainloop()
