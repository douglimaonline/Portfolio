import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image

root = tk.Tk()
root.title("🔑")
root.minsize(width=400, height=450)
# root.config(padx=10)
style = ttk.Style("darkly")

title_text = ttk.Labelframe(text="🔑 Gerador de Senhas")
title_text.place(x=10, y=10, width=380, height=430)

password = ttk.Label(text="Hu&*6b%Lk(H32", font=("TkDefaultFont", 25, "bold"))
password.place(x=20, y=30)

# Copy button
img_copy = Image.open("copy-64.png")  # Replace "image.jpg" with your image file name and extension
resized_img_copy = img_copy.resize((15, 15))  # Replace "width" and "height" with desired size
img_obj_copy = ImageTk.PhotoImage(resized_img_copy)

copy_button = ttk.Checkbutton(image=img_obj_copy, bootstyle="dark-outline-toolbutton")
copy_button.place(x=285, y=40)

# Restart button
img_restart = Image.open("restart-64.png")  # Replace "image.jpg" with your image file name and extension
resized_img_restart = img_restart.resize((15, 15))  # Replace "width" and "height" with desired size
img_obj_restart = ImageTk.PhotoImage(resized_img_restart)

copy_button = ttk.Checkbutton(image=img_obj_restart, bootstyle="dark-outline-toolbutton")
copy_button.place(x=335, y=40)

# repeat_button = ttk.Button(text="🔁")
# repeat_button.grid(column=7, row=1, padx=2)
#
# AZ_checkbutton = ttk.Checkbutton(text="A-Z")
# AZ_checkbutton.grid(column=0, row=3, padx=25, sticky=W)
#
# az_checkbutton = ttk.Checkbutton(text="az")
# az_checkbutton.grid(column=1, row=3, sticky=W)
#
# number_checkbutton = ttk.Checkbutton(text="0-9")
# number_checkbutton.grid(column=2, row=3, sticky=W)
#
# teste = tk.LabelFrame(text="teste", relief="solid", width=50, height=50)
# teste.grid(column=0, row=4)

root.mainloop()
