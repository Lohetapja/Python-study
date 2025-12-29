import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Lohe Calculator")
window.geometry("350x350")

frame = tk.Frame(window)
frame.grid(row=1, column=0, pady=(50, 0), padx=50, columnspan=2)

entry = tk.Entry(window, width=16, font=("Arial", 18))
entry.grid(row=0, column=0, pady=10, padx=50, columnspan=2)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]


for i, button in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    if button == '=':
        tk.Button(frame, text=button, command=calculate, height=2, width=6,).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(frame, text=button, command=clear_entry, height=2, width=6).grid(row=row, column=col)
    else:
        tk.Button(frame, text=button, command=lambda button=button: button_click(button), height=2, width=6).grid(row=row, column=col)

window.columnconfigure(0, weight=1)

window.mainloop()
