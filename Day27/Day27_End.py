from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=100, y=200) # 위젯의 구체적인 위치를 특정하기(위젯이 많으면 비효율적이다.)
my_label.grid(column=0, row=0) # grid와 pack은 같이 쓸 수 없다.
my_label.config(padx=50, pady=50)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me2", command=button_clicked)
new_button.grid(column=2, row=0)


#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)








window.mainloop()