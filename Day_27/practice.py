from tkinter import *

def button_click():
    print("Button got clicked")
    my_label["text"] = input.get()

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New text!")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

#Button
button = Button(text="Click Me", command=button_click)
#button.pack()
button.grid(column=1, row=1)

button_2 = Button(text="Click Me!!", command=button_click)
button_2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()