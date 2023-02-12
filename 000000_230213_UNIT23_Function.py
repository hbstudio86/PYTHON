## UNIT 29 함수 사용하기 ##

#>> 문법
#   def 함수이름():
#       내용...
#   def는 define의 약어 이다.

# 1. 함수 만들기

def hello():
    print('Hello Wordl!')

hello()

# 2. 동적 함수 만들기

a = 10
b = 20

def add(a,b):
    """이 함수는 두 변수를 더하여 출력하는 간단한 함수임.""" # 이러한 형태를 독스트링(docstrings)라고 하며 함수에 대한 설명을 담고 있다.
    print(a + b)

add(a,b)
add(50,66)

#>> 독스트링 출력하기

print(add.__doc__)
help(add)

# 3. 함수 반환값 출력

def Radd(a,b):
    return a + b

print("1+1의 값은 ",Radd(1,1),"입니다")

#>> C계열의 언어들처럼 역시 Return으로 함수의 값을 반환한다.

# 4. 복수의 함수 반환값 출력
#>> 편리하네,,, 역시... 반환값이 여러개 출력해서...

def add_sub(a,b):
    return a+b,a-b  # 리스트 형식으로 반환하고자 한다면, [...]의 형태로 하면 된다.

x,y = add_sub(10,20)    # <== 이때 리턴된 값의 타입은 튜플로 반환 된다.

print(f"10과 20의 합과 곱은 {x}, {y} 입니다.")


# 5. 함수 호출과정 알아보기
#>> 파이썬은 스택이 반대로 되어 있다 (그럼 스택이아니고 큐 아닌가?)
#   밑에서부터 쌓는게 아니라 위에서부터 쌓고 위에서 부터 사라 진다.

# 심사 문제 #

x, y = map(int, input().split())

def calc(x,y):
    return x+y , x-y, x*y, x/y

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
