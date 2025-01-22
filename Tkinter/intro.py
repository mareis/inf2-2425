import tkinter as tk

def on_click():
    lbl.config(text="Knapp trykket på")

root = tk.Tk()

lbl = tk.Label(root, text="Hello World")
lbl.grid(column=0, row=0)

btn = tk.Button(root, text='Knapp 1', command=on_click)
btn.grid(column=1, row=0)

root.mainloop()



