import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()
root.title("🔑")
root.minsize(width=350, height=450)
# style = ttk.Style("darkly")

title_text = ttk.Label(text="🔑 Gerador de Senhas", bootstyle="secondary")
title_text.grid(column=0, row=0)

password = ttk.Label(text="🔑 Gerador de Senhas", font=("TkDefaultFont", 20, "bold"))
password.grid(column=0, row=1)

root.mainloop()
