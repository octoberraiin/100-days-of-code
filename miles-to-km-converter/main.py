from tkinter import *

# Declarations
def miles_to_km():
    miles = float(miles_text_input.get())
    km = round(miles * 1.60934)
    km_result.config(text=km)

# Window
window = Tk()
window.title("Miles to Km converter")
window.config(padx=50, pady=50)


# Labels

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

# Text Input (entry)

miles_text_input = Entry(width=7)
miles_text_input.grid(column=1, row=0)

# Button

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)





window.mainloop()