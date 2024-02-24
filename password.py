import tkinter as tk
from tkinter import messagebox
import random
import string

#Function used to create a passoword 
def generate_password():
    length = int(length_entry.get())
    if length < 8:
        messagebox.showerror("Error", "Password length must be at least 8 characters.")
        return

    complexity_options = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    selected_options = [option.get() for option in complexity_vars]

    characters = ''
    for index, option in enumerate(selected_options):
        if option:
            characters += complexity_options[index]

    if not characters:
        messagebox.showerror("Error", "Please select at least one complexity option.")
        return

    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

#Function able to  copy the password
    
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")

#Python GUI for Interface
root = tk.Tk()
root.title("Password Generator")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

length_label = tk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")

length_entry = tk.Entry(main_frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

complexity_label = tk.Label(main_frame, text="Password Complexity:")
complexity_label.grid(row=1, column=0, sticky="w")

complexity_options = ["Lowercase Letters", "Uppercase Letters", "Numbers", "Special Characters"]
complexity_vars = [tk.BooleanVar() for _ in range(len(complexity_options))]

for i, option in enumerate(complexity_options):
    tk.Checkbutton(main_frame, text=option, variable=complexity_vars[i]).grid(row=i+1, column=1, sticky="w")

generate_button = tk.Button(main_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=5, columnspan=2, pady=10)

password_frame = tk.Frame(root, padx=20, pady=20, bd=2, relief="groove")
password_frame.pack()

password_label = tk.Label(password_frame, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(password_frame, width=30)
password_entry.pack(pady=5)

copy_button = tk.Button(password_frame, text="Copy Password", command=copy_password)
copy_button.pack()

root.mainloop()
