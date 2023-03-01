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


# 1. 함수안에 함수를 정의하기

def helloworld():
    hello = "hello world!"
    def world():
        print(hello)
    world()
helloworld()

#>> 함수안에 함수를 정의 하고 실행을 시킬 수가 있다

#>> 만약 함수 속의 함수가 외부 함수의 변수를 접근하고자 한다면... nonlocal을 사용하라

def a():    # 외부 함수 a
    xx = 10
    def b():
        xx = 20     # 내부 함수 b의 지역변수 xx에 20을 할당해도
    b()             # 실행을 하여도
    print(xx)       # 출력은 외부 함수에 있는 변수 xx값이 출력 된다.

a()

def c():
    xxx = 10
    yyy = 30
    def d():
        nonlocal xxx    # 지역변수가 아니다!인 nonlocal을 사용하면 외부 함수의 xxx를 재정의 할 수 있다.
        xxx = 30        # 역시 C/C++의 extern 개념과 일치한다.
        print(yyy)
    d()
    print(xxx)

c()

# nonlocal은 가장 가까운 외부 함수의 변수를 지정 한다.


# 2. 클로저 사용하기

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()  # calc()라는 함수가 실행되고 변수가 할당되고 내부 함수가 정의 된다음
            # 객체 덩어리 전체를 c에 보낸다.
            # 함수 포인터 느낌도 나고 오묘하다...

print(c(1),c(2),c(3),c(4))

# 3. 람다를 이용하여 클로저 만들기

def calc2():
    aa = 3
    bb = 5
    return lambda x : aa * x + bb

cc = calc2()

print(cc(1),cc(2),cc(3))    # cc,1이 아니네? ㅋ

# 클로저는 함수를 둘러싼 환경을 기억하고 있다가 나중에 다시 사용한다. 함수 매크로의 성격도 가지고 있네 ㅎㅎ;;

# C에서의 함수 매크로
# #define FUNC1(x) (x)+(2)


# 심사 문제 #

def countdown(n):
    count_n = n + 1
    def reduce_n():
        nonlocal count_n
        count_n -= 1
        return count_n
    return reduce_n

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')
