sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
words = sentence.split() # 문자열 쪼개고 리스트로 저장
print(words) # 단어 쪼개졌는지 확인
result = {word: len(word) for word in words}



print(result)