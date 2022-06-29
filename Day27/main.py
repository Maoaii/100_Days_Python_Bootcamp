from tkinter import *

# Screen setup
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def convert_miles_km():
    miles = float(miles_entry.get())
    km = miles * 1.609
    converted_label.config(text=f"{km}")


# Entry
miles_entry = Entry(width=8)
miles_entry.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Equals to label
equals_to_label = Label(text="is equal to")
equals_to_label.grid(column=0, row=1)

# Converted label
converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

# Km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=convert_miles_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
