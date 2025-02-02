import random
import string
import tkinter as tk
from tkinter import messagebox

# Password generator function (same as before)
def generate_password(length=12, use_symbols=True):
    letters = string.ascii_letters  # A-Z, a-z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # Special characters like !, @, #, $

    char_set = letters + digits
    if use_symbols:
        char_set += symbols

    password = ''.join(random.choice(char_set) for _ in range(length))

    return password

# Function to handle the button click
def generate_and_display_password():
    try:
        # Get the length from the input box and ensure it's an integer
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Input Error", "Password length should be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")
        return

    # Get the user's choice for including symbols
    use_symbols = symbols_var.get()

    # Generate the password
    password = generate_password(length, use_symbols)

    # Display the generated password
    password_label.config(text=f"Generated Password: {password}")

# Set up the Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Set window size
root.geometry("400x300")

# Add a label and entry for password length
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Set default length to 12

# Add a checkbox to include symbols
symbols_var = tk.BooleanVar(value=True)  # Default is True (include symbols)
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.pack(pady=10)

# Add a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

# Add a label to display the generated password
password_label = tk.Label(root, text="Generated Password: ")
password_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
