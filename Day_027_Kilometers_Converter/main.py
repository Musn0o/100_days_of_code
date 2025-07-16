from tkinter import Tk, Entry, Label, Button, StringVar

KM_IN_MILE = 1.609


# --- Functionality ---
def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = miles * KM_IN_MILE
        result_var.set(f"{km:.2f}")
    except ValueError:
        result_var.set("Invalid")


def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()


def apply_theme():
    bg = "#121212" if dark_mode else "#FFFFFF"
    fg = "#E0E0E0" if dark_mode else "#000000"
    entry_bg = "#1E1E1E" if dark_mode else "#FFFFFF"
    entry_fg = "#FFFFFF" if dark_mode else "#000000"
    button_bg = "#333333" if dark_mode else "#4285F4"
    button_fg = "#FFFFFF"
    active_bg = "#555555" if dark_mode else "#3367D6"

    window.config(bg=bg)
    for widget in [
        miles_input,
        miles_label,
        is_equal_label,
        kilometer_result_label,
        kilometer_label,
        calculate_button,
        dark_mode_button,
    ]:
        widget.config(bg=bg, fg=fg)

    miles_input.config(bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
    calculate_button.config(bg=button_bg, activebackground=active_bg)
    dark_mode_button.config(bg=button_bg, activebackground=active_bg)


# --- GUI Setup ---
window = Tk()
window.title("Miles to Kilometers")
window.config(padx=40, pady=30)
window.resizable(False, False)

dark_mode = False  # Initial theme state

# Entry
miles_input = Entry(width=10, justify="right", font=("Arial", 14))
miles_input.grid(column=1, row=0, padx=10, pady=10)
miles_input.focus()

# Labels
miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 14))
is_equal_label.grid(column=0, row=1)

result_var = StringVar(value="0.00")
kilometer_result_label = Label(textvariable=result_var, font=("Arial", 14, "bold"))
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=("Arial", 14))
kilometer_label.grid(column=2, row=1)

# Buttons
calculate_button = Button(
    text="Convert",
    command=miles_to_km,
    font=("Arial", 12, "bold"),
    relief="flat",
    padx=10,
    pady=5,
)
calculate_button.grid(column=1, row=2, pady=(15, 5))

dark_mode_button = Button(
    text="Toggle Dark Mode",
    command=toggle_dark_mode,
    font=("Arial", 10),
    relief="flat",
    padx=6,
    pady=3,
)
dark_mode_button.grid(column=1, row=3, pady=5)

# Apply initial theme
apply_theme()

window.mainloop()
