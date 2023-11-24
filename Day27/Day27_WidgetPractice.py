from tkinter import *

# 새 창 생성 및 설정
window = Tk()
window.title("위젯 예제")
window.minsize(width=500, height=500)

# 레이블
label = Label(text="이것은 예전 텍스트입니다.")
label.config(text="이것은 새로운 텍스트입니다.")
label.pack()


# 버튼
def action():
    print("어떤 작업 수행")


# 버튼을 누르면 action() 호출
button = Button(text="클릭하세요", command=action)
button.pack()

# 엔트리
entry = Entry(width=30)
# 처음에 일부 텍스트 추가
entry.insert(END, string="시작할 텍스트입니다.")
# 엔트리에서 텍스트 가져오기
print(entry.get())
entry.pack()

# 텍스트
text = Text(height=5, width=30)
# 텍스트 상자에 커서 놓기
text.focus()
# 처음에 일부 텍스트 추가
text.insert(END, "여러 줄 텍스트 입력의 예제입니다.")
# 텍스트 상자의 현재 값 가져오기 (1행 0열부터)
print(text.get("1.0", END))
text.pack()


# 스핀박스
def spinbox_used():
    # 스핀박스의 현재 값 가져오기
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# 스케일
# 현재 스케일 값으로 호출
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# 체크버튼
def checkbutton_used():
    # 체크 버튼이 선택된 경우 1을 출력, 그렇지 않으면 0을 출력
    print(checked_state.get())


# 선택 상태를 유지하기 위한 변수, 0은 해제, 1은 선택
checked_state = IntVar()
checkbutton = Checkbutton(text="켜져 있나요?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# 라디오버튼
def radio_used():
    print(radio_state.get())


# 어떤 라디오 버튼 값이 선택되었는지 유지하기 위한 변수
radio_state = IntVar()
radiobutton1 = Radiobutton(text="옵션1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="옵션2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# 리스트박스
def listbox_used(event):
    # 리스트박스에서 현재 선택한 항목 가져오기
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["사과", "배", "오렌지", "바나나"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
