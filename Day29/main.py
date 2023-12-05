from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_et.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_et.get()
    email_username = email_username_et.get()
    password = password_et.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oh no!", message="빈칸을 모두 채워주세요!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"다음과 같이 저장하시겠습니까?: \nEmail:{email_username} \nPassword: {password} \n진짜 저장하실꺼죠? ")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email_username} | {password}\n")
                website_et.delete(0, END)
                password_et.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Label
website_lb = Label(text="Website:")
website_lb.grid(column=0, row=1)

email_username_lb = Label(text="Email/Username:")
email_username_lb.grid(column=0, row=2)

password = Label(text="Password: ")
password.grid(column=0, row=3)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Button
password_bt = Button(text="Generate Password", command=generate_password)
password_bt.grid(column=2, row=3)

add_bt = Button(text="Add", width=36, command=save)
add_bt.grid(column=1, row=4, columnspan=2)

# Entry
website_et = Entry(width=35)
website_et.grid(column=1, row=1, columnspan=2)
website_et.focus()

email_username_et = Entry(width=35)
email_username_et.grid(column=1, row=2, columnspan=2)
email_username_et.insert(0, "msh9911@naver.com")

password_et = Entry(width=21)
password_et.grid(column=1, row=3, columnspan=1)

window.mainloop()
