import json
from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oh no!", message="빈칸을 모두 채워주세요!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # 기존 데이터를 읽는다.
                data = json.load(data_file)  # json.load: 이 함수는 json 파일을 파이썬 딕셔너리로 변환해준다.
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # 예전 데이터를 새로운 데이터로 업데이트 한다.
            data.update(new_data)  # load에서 변환된 딕셔너리를 새로운 데이터로 업데이트한다.

            with open("data.json", "w") as data_file:
                # 업데이트 된 데이터를 저장한다.
                json.dump(data, data_file,
                          indent=4)  # json.dump: 이 함수는 설정해놓은 양식대로 json 파일을 작성해준다. / indent: JSON 데이터에 들여쓰기 할 공백을 제공해서 읽기 쉽게 해준다.
        finally:
            website_et.delete(0, END)
            password_et.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_et.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="데이터 파일을 찾을 수 없습니다.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"{website}에 대한 정보가 존재하지 않습니다.")


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

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

# Entry
website_et = Entry(width=21)
website_et.grid(column=1, row=1)
website_et.focus()

email_username_et = Entry(width=35)
email_username_et.grid(column=1, row=2, columnspan=2)
email_username_et.insert(0, "msh9911@naver.com")

password_et = Entry(width=21)
password_et.grid(column=1, row=3, columnspan=1)

window.mainloop()
