#암호를 복호화 시키기
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1: decrypt라는 함수를 만드세요. decrypt는 text의 입력 값을 shift의 값만 큼 뒤로 이동시키고 복호화 된 문자를 출력시키는 함수입니다.
def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


  #TODO-2: decrypt 함수에는 다음과 같은 내용을 통해 실행되어야 합니다.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: direction에 변수에 맞춰 encode라고 치면 암호화로, decode라 치면 복호화로 갈 수 있도록 해보세요.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
if direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)