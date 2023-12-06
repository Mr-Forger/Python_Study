# eval() 함수는 입력을 사용하여 딕셔너리의 리스트를 생성합니다.
facebook_posts = eval(input())

total_likes = 0
# TODO: KeyError 예외를 처리하세요
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError: #키의 다른 요소들은 넘어간다.
        pass

print(total_likes)
