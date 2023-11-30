from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Label
website = Label(text="Website:")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

password = Label(text="Password: ")
password.grid(column=0, row=3)

#Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)



#Button
password_bt = Button(text="Generate Password")
password_bt.grid(column=2, row=3)

add_bt = Button(text="Add", width=35)
add_bt.grid(column=1, row=4, columnspan=2)


#Entry
website_et = Entry(width=35)
website_et.grid(column=1, row=1, columnspan=2)
website_et.focus()

email_username_et = Entry(width=35)
email_username_et.grid (column=1, row=2, columnspan=2)
email_username_et.insert(0, "msh9911@naver.com")

password_et = Entry(width=21)
password_et.grid(column=1, row=3, columnspan=1)








window.mainloop()