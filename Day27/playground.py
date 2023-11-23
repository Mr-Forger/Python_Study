def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum


# add(3, 5, 6)
print(add(3, 5, 6, 2, 1, 7, 4, 3))


def calculate(n, **kwargs):  # 가변 키워드 인수
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])  # 딕셔너리의 value 뽑기
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=20)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


def test(*args):
    print(args)


test(1, 2, 3, 4)
