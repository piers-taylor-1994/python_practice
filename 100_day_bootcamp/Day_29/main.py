from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    # password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    # password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if not website or not password:
        messagebox.showerror("Oops", "Please don't leave any fields empty!")
    else:
        try:
            with open("Day_29/data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            open("Day_29/data.json", "w")
            data = new_data
        finally:
            with open("Day_29/data.json", "w") as file:
                json.dump(data, file, indent=4)

                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    website = website_input.get()
    if not website:
        messagebox.showwarning("Website missing", "Please enter a website")
    else:
        try:
            with open("Day_29/data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(f"Websites", f"No websites have been recorded yet")
        else:
            try:
                messagebox.showinfo(f"{website}", f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
            except:
                messagebox.showwarning(f"{website}", f"Cannot find recorded email/password data for {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(height=1000, width=1000, padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="Day_29/logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "piers.taylorr@gmail.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1)
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

window.mainloop()