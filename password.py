import tkinter as tk
from tkinter import ttk
import random
import string

def password_generator(size=12, complexity=1, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
    if complexity == 1:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    elif complexity == 2:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    elif complexity == 3:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(size))

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x200")

        self.size_var = tk.IntVar()
        self.size_var.set(12)

        self.complexity_var = tk.IntVar()
        self.complexity_var.set(1)

        self.label = ttk.Label(self, text="Size:")
        self.label.pack(pady=10)

        self.spinbox = ttk.Spinbox(self, from_=8, to=25, textvariable=self.size_var)
        self.spinbox.pack(pady=10)

        self.complexity_label = ttk.Label(self, text="Complexity:")
        self.complexity_label.pack(pady=10)

        self.complexity_combobox = ttk.Combobox(self, textvariable=self.complexity_var, values=[1, 2, 3])
        self.complexity_combobox.pack(pady=10)

        self.button = ttk.Button(self, text="Generate", command=self.generate_password)
        self.button.pack(pady=10)

        self.password_var = tk.StringVar()

        self.password_label = ttk.Label(self, textvariable=self.password_var)
        self.password_label.pack(pady=10)

    def generate_password(self):
        size = self.size_var.get()
        complexity = self.complexity_var.get()
        password = password_generator(size, complexity)
        self.password_var.set(password)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()