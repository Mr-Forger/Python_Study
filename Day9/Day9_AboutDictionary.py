programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

#dictionary에서 요소를 호출하는 방법
print(programming_dictionary["Bug"])

#dictionary에 새로운 요소를 코드로 추가 하는 방법
programming_dictionary["Korea"] = "The Nation in East Asia."

#비어있는 새로운 dictionary를 만드는 방법
emptyDictionary = {}

#존재하는 dictionary를 없애는 방법
# programming_dictionary = {}
# print(programming_dictionary)

#dictionary안의 값을 수정하는 방법
programming_dictionary["Bug"] = "A moth in everywhere"
print(programming_dictionary["Bug"])

#dictionary를 통해 반복문 돌리기
for thing in programming_dictionary:
    print(thing) #이때는 key 만 출력한다.
    print(programming_dictionary[thing]) #이떄는 Value만 출력한다.