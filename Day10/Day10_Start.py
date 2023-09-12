#출력을 가지는 함수
# def formatName(fName, lName):
#     formatFName = fName.title()
#     formatLName = lName.title()

#     print(f"{formatFName} {formatLName}")

# formatName("MOON", "SeunGHAN")

#리턴 값 출력시키기
def formatName(fName, lName):
    formatFName = fName.title()
    formatLName = lName.title()

    return f"{formatFName} {formatLName}"

print(formatName("MOON", "SeunGHAN")) #print에 함수 자체를 박아넣는다.