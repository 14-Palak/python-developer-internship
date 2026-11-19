
import tkinter as tk

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Calculator | Python Project")
root.geometry("360x520")
root.resizable(False, False)
root.configure(bg="#151522")

# Store the current expression
expression = ""


# ---------------- DISPLAY ----------------

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 28, "bold"),
    bg="#222236",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)

display.pack(
    padx=20,
    pady=(30, 20),
    fill="x",
    ipady=22
)


# ---------------- BUTTON FUNCTIONS ----------------

def button_click(value):
    global expression

    if display_var.get() == "Error":
        expression = ""

    expression += str(value)
    display_var.set(expression)


def clear():
    global expression
    expression = ""
    display_var.set("")


def delete():
    global expression

    expression = expression[:-1]
    display_var.set(expression)


def calculate():
    global expression

    try:
        if not expression:
            return

        # Only allow calculator characters
        allowed = "0123456789+-*/.() "

        if any(char not in allowed for char in expression):
            raise ValueError("Invalid input")

        result = eval(expression)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display_var.set(str(result))
        expression = str(result)

    except (ValueError, SyntaxError, ZeroDivisionError, TypeError):
        display_var.set("Error")
        expression = ""


# ---------------- BUTTON FRAME ----------------

button_frame = tk.Frame(
    root,
    bg="#151522"
)

button_frame.pack(
    padx=15,
    pady=10,
    fill="both",
    expand=True
)


# ---------------- BUTTON DESIGN ----------------

buttons = [
    ("C", 0, 0, "#dc5b70"),
    ("⌫", 0, 1, "#514b70"),
    ("(", 0, 2, "#514b70"),
    (")", 0, 3, "#514b70"),

    ("7", 1, 0, "#29293d"),
    ("8", 1, 1, "#29293d"),
    ("9", 1, 2, "#29293d"),
    ("/", 1, 3, "#8b5cf6"),

    ("4", 2, 0, "#29293d"),
    ("5", 2, 1, "#29293d"),
    ("6", 2, 2, "#29293d"),
    ("*", 2, 3, "#8b5cf6"),

    ("1", 3, 0, "#29293d"),
    ("2", 3, 1, "#29293d"),
    ("3", 3, 2, "#29293d"),
    ("-", 3, 3, "#8b5cf6"),

    ("0", 4, 0, "#29293d"),
    (".", 4, 1, "#29293d"),
    ("=", 4, 2, "#8b5cf6"),
    ("+", 4, 3, "#8b5cf6")
]


# ---------------- CREATE BUTTONS ----------------

for text, row, column, color in buttons:

    if text == "C":
        command = clear

    elif text == "⌫":
        command = delete

    elif text == "=":
        command = calculate

    else:
        command = lambda value=text: button_click(value)

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 17, "bold"),
        bg=color,
        fg="white",
        activebackground="#a78bfa",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )


# Make all rows and columns equal
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)


# ---------------- RUN APPLICATION ----------------

root.mainloop()
