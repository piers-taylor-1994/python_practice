from tkinter import *

def calculate_km():
    label_3.config(text=round(float(input.get()) / 5 * 8, 2))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)

label = Label(text="Miles")
label.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text=0)
label_3.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

input = Entry(width=10)
input.insert(END, string=0)
input.grid(column=1, row=0)

button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

window.mainloop()