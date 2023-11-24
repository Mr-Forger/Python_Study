from tkinter import *

window = Tk()
window.title("My First Tkinter Program")
window.minsize(500, 300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
button = Button()


window.mainloop()
