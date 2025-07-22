# 파일 제목 'triangle.py'라는 이름으로 저장하기
print('직각삼각형 그리기\n')
leg = int(input('변의 길이: '))

for i in range(leg):
    print('* ' * (i + 1))

area = (leg ** 2) / 2
print('넓이:', area)

# 터미널에서 python triangle.py 라고 명령어 입력시
# 변의 길이를 숫자 기재하면 아래와 같은 결과가 출력됨

# 결과
# 직각삼각형 그리기

# 변의 길이: 4
# *
# * *
# * * *
# * * * *
# 넓이: 8.0