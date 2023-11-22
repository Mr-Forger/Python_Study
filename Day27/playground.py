def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum


# add(3, 5, 6)
print(add(3, 5, 6, 2, 1, 7, 4, 3))


def calculate(**kwargs):  # 가변 키워드 인수
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["multiply"]) # 딕셔너리의 value 뽑기


calculate(add=3, multiply=20)
