from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=f"you said {new_text}")

# Window
window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 25, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="New Text")

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=3)






window.mainloop()