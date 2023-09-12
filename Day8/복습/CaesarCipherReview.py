#암호화 함수 encrypt() 만들기
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: encrypt 함수를 만들고 파라미터로는 text, shift를 가집니다.
def encrypt(plainText, shiftAmount):
    cipherText = ""
    for encoding in plainText: #문자열을 하나씩 따로 받는다. ex) kim => "k", "i", "m"
        position = alphabet.index(encoding) #알파벳에서 plainText의 글자 인덱스를 뜻한다. ex)a = alphabet[0], for문 변수로 받아야한다.
        newPosition = position + shiftAmount
        encodeText = alphabet[newPosition]
        cipherText += encodeText
    print(f"The encoded texdt is {cipherText}.")

    #TODO-2: encrypt 함수에는, shift 시 text로 받은 문자들이 앞으로 이동 후 암호화 된 text를 출력합니다.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: encrypt 함수를 호출하고 출력하세요! 
encrypt(plainText=text, shiftAmount=shift)
