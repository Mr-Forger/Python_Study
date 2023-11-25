from tkinter import *


# miles to km 함수
def convert():
    print("변환하였습니다.")
    miles = miles_input.get()
    convert_km = round(float(miles) / 0.62137)
    miles_to_km.config(text=convert_km)


# window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Label
miles = Label(text=" Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to ")
equal.grid(column=0, row=1)

miles_to_km = Label(text="0")
miles_to_km.grid(column=1, row=1)

km = Label(text=" Km",)
km.grid(column=2, row=1)

# Button
calc = Button(text="Calculate", command=convert)
calc.grid(column=1, row=2)

# Entry
miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=1, row=0)

window.mainloop()
