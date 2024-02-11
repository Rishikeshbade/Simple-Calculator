import tkinter as tk


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def add_to_entry(char):
    entry.insert(tk.END, char)


def clear_entry():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Simple Calculator")


entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]


for (text, row, column) in buttons:
    if text != '=' and text != 'C':
        btn = tk.Button(root, text=text, padx=20, pady=10, command=lambda char=text: add_to_entry(char))
    elif text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=10, command=calculate)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=10, command=clear_entry)
    btn.grid(row=row, column=column, padx=5, pady=5)


root.mainloop()
