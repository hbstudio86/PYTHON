## UNIT21 터틀 그래픽스로 그림 그리기 ##

# 1. 사각형 그리기

import turtle as t
t.shape('turtle')   #turtle이라고 지정해줘야 한다.
#t.shape()   # 지정하지 않으면 세모가 생긴다.
t.forward(100)      # 거북이가 앞으로 이동하면서 선을 긋는다.
t.right(90)         # 우측으로 90도 회전한다.
t.forward(100)      # 이것을 반복한다.
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# forward = fd / backward = bk / left = lt / right = rt
# 창이 바로 사라질 경우... : t.mainloop()

# 2. 다각형 그리기

i = 0
for i in range(4):
    t.fd(30)
    t.rt(90)

for i in range(5):  #오각형
    t.fd(80)
    t.rt(360/5)

#n = int(input())

for i in range(6):  #사용자 정의 다각형
    t.fd(80)
    t.rt(360/6)

# 3. 색칠하기

t.color('red')  # 색을 지정합니다. 색상 컬러를 16진수로 표현 가능 '#FF0000' 이런식으로
t.begin_fill()  # 색칠할 영역 시작
for i in range(12):
    t.fd(50)
    t.lt(360/12)
t.end_fill()    # 이것을 하지 않으면 선만 빨간색으로 변한다.

# 4. 원그리기

t.color('#000000')
t.circle(200)   # r이다

t.speed('fastest')  #그리기 속도, fastest 0 / fast 10 / normal 6 / slow 3 / slowest 1 / 숫자는 0.5 ~ 10까지

for i in range(60):
    t.circle(80)
    t.right(360/60)

# 5. 복잡한 무늬

for i in range(300):
    t.forward(i)
    t.right(91)


# 심사 문제 #

t.color('green')

n, line = map(int, input().split())
i = 0

for i in range(n):
    t.right(360/n)
    t.forward(line)
