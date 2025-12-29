import tkinter as tk    # Import the Tkinter module

def button_click(value):
    entry.insert(tk.END, str(value))


window = tk.Tk()          # Create an instance of the Tk class, HERE COMES THE MAIN WINDOW
window.title("Lohe Calculaator") # # Set the title of the window, HERE COMES THE TITLE OF THE WINDOW
window.geometry("400x500") # Set the size of the window, HERE COMES THE SIZE OF THE WINDOW      ##  pack() or pack()  bit not both


frame = tk.Frame(window)
frame.pack(side=tk.BOTTOM)

# Buttons are created here

entry = tk.Entry(window, width=16, font= ("Arial", 18))
entry.pack(pady=10)


buttons = [
    tk.Button(frame, text=str(i), command=lambda i=i:button_click(i), height=2, width=6)
    for i in range(10)
]+[
    tk.Button(frame,text=symbol, command=lambda symbol=symbol:button_click(symbol), height=2, width=6)
    for symbol in ['+','-','*','/','=','C']
]

for i, button in enumerate(buttons):
    button.grid(row=int(i/4), column=i%4, padx=8, pady=8)

window.mainloop()         # Start the event loop, HERE COMES THE MAINLOOP METHOD that is used to start the event loop, that is for the window to be displayed

