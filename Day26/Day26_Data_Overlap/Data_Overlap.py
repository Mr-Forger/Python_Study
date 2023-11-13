# # 내 풀이
# with open("file1.txt") as data:
#     numbers = data.readlines()
#     data1 = [int(n.strip()) for n in numbers]
#
# with open("file2.txt") as data:
#     numbers = data.readlines()
#     data2 = [int(n.strip()) for n in numbers]
#
# result = [n for n in data1 if n in data2]
# print(result)

# 솔루션
with open("file1.txt") as data:
    data1 = data.readlines()

with open("file2.txt") as data:
    data2 = data.readlines()

result = [int(n) for n in data1 if n in data2]
print(result)
