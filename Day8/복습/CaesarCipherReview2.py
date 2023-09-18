from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: caesar 함수를 만들고 파라미터로는 text, shift, direction을 가집니다.
def caesar(plain_text, shift_amount, cipher_direction):
    final_text = "" #최종 암호화 문자 변
    if cipher_direction == "decode":
        shift_amount *= -1 #디코딩 시에는 -1을 곱한다.
    for letter in plain_text:
        if letter in alphabet: #for문 변수(plain_text의 각 문자열 한개)가 알파벳 안에 있을때 / 숫자나 특수기호 썻을때는 문자를 이동시키게 하는 것을 방지한다.
            start_position = alphabet.index(letter) #알파벳 리스트 안에서의 각 문자열 하나의 인덱스 번호
            new_postiion = start_position + shift_amount
            final_text += alphabet[new_postiion]
        else:
            final_text += letter
    print(f"{cipher_direction}을 통해 암호화 된 문자는 {final_text}입니다.")
    
    





 #TODO-2: caesar 함수에는, encoding, decoding중 어느 것을 할지 선택 후 shift만큼 이동 후 암호화 된 text를 출력합니다.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"



#TODO-3: caesar 함수를 호출하고 출력하세요! 
#caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

#심화: no라고 치기 전까지 계속해서 반복 되도록 해주세요.
flag = True
while flag:   
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") #인코딩 디코딩 선택
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #알파벳보다 큰 수를 넣었을때, 이 수를 0에서 25사이의 범위로 만들어주도록 바꿔주세요.
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction) #함수 실행

    if input("다시하실꺼면 yes, 아니면 no를 입력해주세요: ") == "no":
        flag = False
        print("goodbye")
    #yes 입력 시 while문 첫 문장으로 다시 돌아간다.

    
