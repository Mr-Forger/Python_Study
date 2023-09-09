alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: encrypt, decrypt 함수를 없애고 하나로 합쳐진 caesar()함수를 만드세요
def caesar(startText, shiftAmount, selDirection):
    endText = ""
    if selDirection == "decode":
        shiftAmount *= -1
    for letter in startText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        endText += alphabet[newPosition]
    print(f"The {selDirection}d text is {endText}.")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(startText=text, shiftAmount=shift, selDirection=direction)