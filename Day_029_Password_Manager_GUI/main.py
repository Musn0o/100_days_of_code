import string
import json
import pyperclip
from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage, END
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- CONSTANTS ------------------------------- #
DATA_FILE = "Day_029_Password_Manager_GUI/data.json"
LOGO_PATH = "Day_029_Password_Manager_GUI/logo.png"
DEFAULT_EMAIL = "scar@gmail.com"


# ---------------------------- PASSWORD MANAGER APP ------------------------------- #
class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.config(padx=50, pady=50)
        self._setup_ui()

    def _setup_ui(self):
        # Logo
        canvas = Canvas(height=200, width=200)
        try:
            self.logo_img = PhotoImage(file=LOGO_PATH)
            canvas.create_image(100, 100, image=self.logo_img)
        except Exception:
            canvas.create_text(
                100, 100, text="Logo\nMissing", font=("Arial", 20, "bold")
            )
        canvas.grid(row=0, column=1)

        # Labels
        Label(text="Website:").grid(row=1, column=0)
        Label(text="Email/Username:").grid(row=2, column=0)
        Label(text="Password:").grid(row=3, column=0)

        # Entries
        self.website_entry = Entry(width=21)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()

        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(0, DEFAULT_EMAIL)

        self.password_entry = Entry(width=21)
        self.password_entry.grid(row=3, column=1)

        # Buttons
        Button(text="Search", width=13, command=self.search).grid(row=1, column=2)
        Button(text="Generate Password", command=self.generate_password).grid(
            row=3, column=2
        )
        Button(text="Add", width=36, command=self.save).grid(
            row=4, column=1, columnspan=2
        )

    def generate_password(self):
        letters = string.ascii_letters
        numbers = string.digits
        symbols = "!#$%&()*+"

        password_chars = (
            [choice(letters) for _ in range(randint(8, 10))]
            + [choice(symbols) for _ in range(randint(2, 4))]
            + [choice(numbers) for _ in range(randint(2, 4))]
        )
        shuffle(password_chars)
        password = "".join(password_chars)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    def save(self):
        website = self.website_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not website or not password:
            messagebox.showinfo(
                title="Oops",
                message="Please make sure you haven't left any fields empty.",
            )
            return

        new_data = {website: {"email": email, "password": password}}

        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?",
        )
        if is_ok:
            try:
                try:
                    with open(DATA_FILE, "r") as data_file:
                        data = json.load(data_file)
                except FileNotFoundError:
                    data = {}
                data.update(new_data)
                with open(DATA_FILE, "w") as data_file:
                    json.dump(data, data_file, indent=4)
                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)
                messagebox.showinfo(
                    title="Success", message="Password saved successfully!"
                )
            except Exception as e:
                messagebox.showerror(title="Error", message=f"Failed to save data: {e}")

    def search(self):
        website = self.website_entry.get().strip()
        if not website:
            messagebox.showinfo(
                title="Oops", message="Please enter a website to search."
            )
            return
        try:
            with open(DATA_FILE, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(
                    title=f"{website}", message=f"Email: {email}\nPassword: {password}"
                )
            else:
                messagebox.showerror(
                    title="Error", message="No Details For The Website Exist."
                )


# ---------------------------- MAIN ------------------------------- #
if __name__ == "__main__":
    root = Tk()
    app = PasswordManager(root)
    root.mainloop()
