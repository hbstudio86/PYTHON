# UNIT33 클로저 사용하기 #

#>> 파이썬도 C/C++과 마찬가지로 함수의 수명이 존재 한다.
#   main 함수가 없으니 제일 위에 있는 변수는 전역 변수 이다
#   block 내 있는 함수는 지역 변수로 수명은 block 내로 국한 되는 것은 동일하다

#   만약 전역 변수를 block 내에서 수정을 하고 싶다면 global 키워드를 사용해야 한다.
#   마치 extern의 느낌이랑 비슷하다고 생각한다.

x = 10

def f1():
    global x
    x = 20
    print(x)
f1()
print(x)
    
#>> 만약 함수내에 global 변수가 오직 하나이면, 그 변수가 전역 변수가 된다.

def f2():
    global y
    y = 30
    print(y)

f2()
y=50
print(y)
f2()
print(y)
