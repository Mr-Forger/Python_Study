with open("file1.txt") as file:
    num = file.readlines()

print(num)

with open("file2.txt") as file:
    num2 = file.readlines()

print(num2)

result = [int(n) for n in num if n in num2]
print(result)

result.sort()
print(result)


