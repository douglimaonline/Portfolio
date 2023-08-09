from tkinter import *

window = Tk()
window.title("Conversor de Milhas para Km")
window.minsize(width=350, height=100)
window.config(padx=20, pady=20)


def convert():
    info_miles = entry.get()
    if "," in info_miles:
        info_miles = info_miles.replace(",", ".")
    result.config(text=str(round(float(info_miles) * 1.60934, 2)).replace(".", ","))


# Entry
entry = Entry()
entry.config(width=10, )
entry.grid(column=1, row=0)

miles = Label(text="Milhas", font=("Arial", 15))
miles.config(padx=10)
miles.grid(column=2, row=0)

answer = Label(text=f"é igual a ", font=("Arial", 15))
miles.config(pady=10)
answer.grid(column=0, row=1)

result = Label(text="", font=("Arial", 15))
result.config(pady=10)
result.grid(column=1, row=1)

km = Label(text="Km.", font=("Arial", 15))
miles.config(pady=10)
km.grid(column=2, row=1)

# Buttons
button1 = Button(text="Calcular", command=convert)
button1.grid(column=1, row=2)

window.mainloop()